python -m pyserini.encode \
  input   --corpus ../../data/corpus/corpus.json \
  output  --embeddings "../../run/1_indexing/sbert" \
          --to-faiss \
  encoder --encoder sentence-transformers/msmarco-bert-base-dot-v5 \
          --batch 64