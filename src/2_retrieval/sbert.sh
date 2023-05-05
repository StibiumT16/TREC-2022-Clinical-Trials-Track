python -m pyserini.search.faiss \
  --index "../../run/1_indexing/sbert" \
  --topics "../../data/query/queries.tsv" \
  --encoder sentence-transformers/msmarco-bert-base-dot-v5 \
  --output "../../run/2_retrieval/sbert/run.tsv" \
  --output-format trec \
  --batch-size 36 --threads 12


python -m pyserini.eval.trec_eval -c \
  -mndcg_cut.10 -mP.5 -mRprec -mrecip_rank \
  ../../data/query/qrels.tsv \
  ../../run/2_retrieval/sbert/run.tsv \
  >> ../../run/2_retrieval/sbert/log