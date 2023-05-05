python -m pyserini.index.lucene \
  --collection JsonCollection \
  --input ../../data/corpus \
  --index "../../run/1_indexing/sparse_pos_docvec" \
  --generator DefaultLuceneDocumentGenerator \
  --threads 128 \
  --storePositions --storeDocvectors --storeRaw