### 3. Relevance Feedback

| Model | NDCG@10 | P@5 | RPrec | MRR |
| :-----------: | :-----------: | :-----------: | :-----------: | :-----------: |
|BM25|0.3608|0.4800|0.2375|0.6398|
|BM25 + Rocchio|**0.3886**|0.4720|**0.2733**|0.5894|
|qld|0.2906|0.3960|0.1698|0.6041|
|qld + Rocchio|0.3758|**0.5000**|0.2588|**0.6760**|

Based on [pyserini](https://github.com/castorini/pyserini)