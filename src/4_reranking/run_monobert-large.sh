#!/bin/bash

set -e

python reranking.py \
    --stage "2_retrieval" \
    --retriever sbert \
    --reranker monobert-large \
    --model_name_or_path castorini/monobert-large-msmarco

python -m pyserini.eval.trec_eval -c \
  -mndcg_cut.10 -mP.5 -mRprec -mrecip_rank \
  ../../data/query/qrels.tsv \
  ../../run/4_reranking/sbert_monobert-large/run.tsv \
  >> ../../run/4_reranking/sbert_monobert-large/log

python reranking.py \
    --stage "2_retrieval" \
    --retriever bm25 \
    --reranker monobert-large \
    --model_name_or_path castorini/monobert-large-msmarco

python -m pyserini.eval.trec_eval -c \
  -mndcg_cut.10 -mP.5 -mRprec -mrecip_rank \
  ../../data/query/qrels.tsv \
  ../../run/4_reranking/bm25_monobert-large/run.tsv \
  >> ../../run/4_reranking/bm25_monobert-large/log

python reranking.py \
    --stage "3_relevance_feedback" \
    --retriever bm25_rocchio \
    --reranker monobert-large \
    --model_name_or_path castorini/monobert-large-msmarco

python -m pyserini.eval.trec_eval -c \
  -mndcg_cut.10 -mP.5 -mRprec -mrecip_rank \
  ../../data/query/qrels.tsv \
  ../../run/4_reranking/bm25_rocchio_monobert-large/run.tsv \
  >> ../../run/4_reranking/bm25_rocchio_monobert-large/log

python reranking.py \
    --stage "3_relevance_feedback" \
    --retriever qld_rocchio \
    --reranker monobert-large \
    --model_name_or_path castorini/monobert-large-msmarco

python -m pyserini.eval.trec_eval -c \
  -mndcg_cut.10 -mP.5 -mRprec -mrecip_rank \
  ../../data/query/qrels.tsv \
  ../../run/4_reranking/qld_rocchio_monobert-large/run.tsv \
  >> ../../run/4_reranking/qld_rocchio_monobert-large/log
