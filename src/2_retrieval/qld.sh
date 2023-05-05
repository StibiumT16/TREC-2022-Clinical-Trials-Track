python -m pyserini.search.lucene \
  --index "../../run/1_indexing/sparse_pos_docvec" \
  --topics "../../data/query/queries.tsv" \
  --output "../../run/2_retrieval/qld/run.tsv" \
  --output-format trec \
  --hits 1000 \
  --qld

python -m pyserini.eval.trec_eval -c \
  -mndcg_cut.10 -mP.5 -mRprec -mrecip_rank \
  ../../data/query/qrels.tsv \
  ../../run/2_retrieval/qld/run.tsv \
  >> ../../run/2_retrieval/qld/log