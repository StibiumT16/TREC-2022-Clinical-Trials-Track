import os
import json
import torch
import argparse
from tqdm import tqdm
from pygaggle.rerank.base import Query, Text
from pygaggle.rerank.transformer import MonoT5, MonoBERT
from transformers import T5ForConditionalGeneration, AutoModelForSequenceClassification, AutoTokenizer, T5Tokenizer

device = torch.device("cuda:0")
parser = argparse.ArgumentParser()
parser.add_argument("--stage", default="2_retrieval", type=str, choices=['2_retrieval', '3_relevance_feedback'])
parser.add_argument("--retriever", default="bm25", type=str)
parser.add_argument("--reranker", default="monot5-3b", type=str, choices=['monot5-base', 'monot5-large', 'monot5-3b', 'monobert-base', 'monobert-large'])
parser.add_argument("--model_name_or_path", default="castorini/monot5-3b-msmarco-10k", type=str)
args = parser.parse_args()


topk = 1000
query_file = "../../data/query/queries.tsv"
corpus_file = "../../data/corpus/corpus.json"
run_path = f"../../run/{args.stage}/{args.retriever}/run.tsv"
out_path = f"../../run/4_reranking/{args.retriever}_{args.reranker}/"

def get_run(corpus_file, run_path):
    content_dict = {}
    with open(corpus_file) as fin:
        for line in fin:
            line = json.loads(line)
            did, content = line['id'], line['contents']
            content_dict[did] = content.lower().strip()
    
    dids_dict, docs_dict = {}, {}
    with open(run_path) as fin:
        for line in fin:
            qid, _, did, _, _, _ = line.strip().split()
            if qid not in dids_dict:
                dids_dict[qid] = [did]
                docs_dict[qid] = [content_dict[did]]
            else:
                dids_dict[qid].append(did)
                docs_dict[qid].append(content_dict[did])
        return dids_dict, docs_dict



if __name__ == '__main__':
    dids_dict, docs_dict = get_run(corpus_file, run_path)
    if args.reranker.find('t5') != -1:
        reranker = MonoT5(args.model_name_or_path)
    elif args.reranker.find('bert') != -1:
        model = AutoModelForSequenceClassification.from_pretrained(args.model_name_or_path)
        tokenizer = AutoTokenizer.from_pretrained(args.model_name_or_path)
        model = model.to(device).eval()
        reranker = MonoBERT(model=model,tokenizer=tokenizer)
        
    if not os.path.exists(out_path):
        os.mkdir(out_path)
    with open(query_file, "r") as fr, open(out_path+"/run.tsv", "w") as fw:
        for line in tqdm(fr):
            qid, query = line.strip().split("\t")
            query = Query(query)
            dids, docs = dids_dict[qid], docs_dict[qid]
            psgs = [[dids[i], docs[i]] for i in range(len(dids))]
            texts = [Text(p[1], {'docid': p[0]}, 0) for p in psgs]
            reranked = reranker.rerank(query, texts)
            
            for i in range(topk):
                fw.write(qid + " Q0 " + reranked[i].metadata["docid"] + " " + str(i + 1) + " " + str(reranked[i].score) + " " + args.retriever+ "_" + args.reranker + "\n")