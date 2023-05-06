import os
import numpy as np

topk = 1000

mnz_or_sum = "mnz" #mnz or sum

run_paths = ['../../run/4_reranking/bm25_monot5-3b/run.tsv', '../../run/4_reranking/sbert_monobert-large/run.tsv','../../run/4_reranking/qld_rocchio_monot5-3b/run.tsv']
out_path = f"../../run/5_fusion/comb{mnz_or_sum}"

comb_scores = [{} for i in range(50)]

for run_path in run_paths:
    with open(run_path, 'r') as fin:
        for line in fin:
            qid, _, did, rk, score, _ = line.split()
            if int(rk) == 1:
                dids = [did]
                scores = [float(score)]
                continue
            dids.append(did)
            scores.append(float(score))
            if int(rk) == topk:
                normalized = [((np.exp(it) - np.exp(scores[-1])) / (np.exp(scores[0]) - np.exp(scores[-1]))) for it in scores]
                pos = int(qid) - 1
                for did, score in zip(dids, normalized):
                    if did not in comb_scores[pos]:
                        comb_scores[pos][did] = [score]    
                    else:
                        comb_scores[pos][did].append(score)


if not os.path.exists(out_path):
    os.mkdir(out_path)

with open(out_path + '/run.tsv', 'w') as fw:
    for i, comb_score in enumerate(comb_scores):
        tmp = {}
        qid = str(i + 1)
        if mnz_or_sum == 'mnz':
            for k, v in comb_score.items():
                tmp[k] = np.sum(v) * len(v)
        elif mnz_or_sum == 'sum':
            for k, v in comb_score.items():
                tmp[k] = np.sum(v)
        sorted_list = sorted(tmp.items(), key = lambda x : x[1], reverse = True)[:topk]
        for j, it in enumerate(sorted_list):
            fw.write(qid + " Q0 " + it[0] + " " + str(j + 1) + " " + str(it[1]) + f" comb{mnz_or_sum}\n")

os.system(f"python -m pyserini.eval.trec_eval -c \
            -mndcg_cut.10 -mP.5,10 -mRprec -mrecip_rank \
            ../../data/query/qrels.tsv \
            ../../run/5_fusion/comb{mnz_or_sum}/run.tsv \
            >> {out_path}/log")