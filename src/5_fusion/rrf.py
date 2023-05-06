import os

k = 10
topk = 1000
run_paths = ['../../run/4_reranking/bm25_monot5-3b/run.tsv', '../../run/4_reranking/sbert_monobert-large/run.tsv','../../run/4_reranking/qld_rocchio_monot5-3b/run.tsv']
out_path = f"../../run/5_fusion/rrf_{k}/"
rrf_scores = [{} for i in range(50)]

for run_path in run_paths:
    with open(run_path, 'r') as fin:
        for line in fin:
            qid, _, did, rk, _, _ = line.split()
            pos = int(qid) - 1
            if did not in rrf_scores[pos]:
                rrf_scores[pos][did] = 1 / (int(rk) + k)
            else:
                rrf_scores[pos][did] += 1 / (int(rk) + k)

if not os.path.exists(out_path):
    os.mkdir(out_path)

with open(out_path + '/run.tsv', 'w') as fw:
    for i, rrf_score in enumerate(rrf_scores):
        qid = str(i + 1)
        sorted_list = sorted(rrf_score.items(), key = lambda x : x[1], reverse = True)[:topk]
        for j, it in enumerate(sorted_list):
            fw.write(qid + " Q0 " + it[0] + " " + str(j + 1) + " " + str(it[1]) + f" rrf_{k}\n")

os.system(f"python -m pyserini.eval.trec_eval -c \
            -mndcg_cut.10 -mP.5,10 -mRprec -mrecip_rank \
            ../../data/query/qrels.tsv \
            ../../run/5_fusion/rrf_{k}/run.tsv \
            >> {out_path}/log")
