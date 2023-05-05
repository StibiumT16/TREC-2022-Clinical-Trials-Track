#!/bin/bash

set -e

python reranking.py \
    --stage "2_retrieval" \
    --retriever sbert \
    --reranker monot5-large \
    --model_name_or_path castorini/monot5-large-msmarco-10k

python -m pyserini.eval.trec_eval -c \
  -mndcg_cut.10 -mP.5 -mRprec -mrecip_rank \
  ../../data/query/qrels.tsv \
  ../../run/4_reranking/sbert_monot5-large/run.tsv \
  >> ../../run/4_reranking/sbert_monot5-large/log

python reranking.py \
    --stage "2_retrieval" \
    --retriever bm25 \
    --reranker monot5-large \
    --model_name_or_path castorini/monot5-large-msmarco-10k

python -m pyserini.eval.trec_eval -c \
  -mndcg_cut.10 -mP.5 -mRprec -mrecip_rank \
  ../../data/query/qrels.tsv \
  ../../run/4_reranking/bm25_monot5-large/run.tsv \
  >> ../../run/4_reranking/bm25_monot5-large/log

python reranking.py \
    --stage "3_relevance_feedback" \
    --retriever bm25_rocchio \
    --reranker monot5-large \
    --model_name_or_path castorini/monot5-large-msmarco-10k

python -m pyserini.eval.trec_eval -c \
  -mndcg_cut.10 -mP.5 -mRprec -mrecip_rank \
  ../../data/query/qrels.tsv \
  ../../run/4_reranking/bm25_rocchio_monot5-large/run.tsv \
  >> ../../run/4_reranking/bm25_rocchio_monot5-large/log

python reranking.py \
    --stage "3_relevance_feedback" \
    --retriever qld_rocchio \
    --reranker monot5-large \
    --model_name_or_path castorini/monot5-large-msmarco-10k

python -m pyserini.eval.trec_eval -c \
  -mndcg_cut.10 -mP.5 -mRprec -mrecip_rank \
  ../../data/query/qrels.tsv \
  ../../run/4_reranking/qld_rocchio_monot5-large/run.tsv \
  >> ../../run/4_reranking/qld_rocchio_monot5-large/log
