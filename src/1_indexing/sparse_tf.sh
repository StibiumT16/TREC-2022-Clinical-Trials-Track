python -m pyserini.index.lucene \
  --collection JsonCollection \
  --input ../../data/corpus \
  --index "../../run/1_indexing/sparse_tf" \
  --generator DefaultLuceneDocumentGenerator \
  --threads 128 \
  --storeDocvectors --storeRaw