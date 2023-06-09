### 4. Reranking

| Model | NDCG@10 | P@5 | RPrec | MRR |
| :-----------: | :-----------: | :-----------: | :-----------: | :-----------: |
|BM25|0.3608|0.4800|0.2375|0.6398|
|BM25 + MonoBERT-large|0.4438|0.5840|0.2829|0.7172|
|BM25 + MonoT5-large|0.1094|0.1280|0.2009|0.2703|
|BM25 + MonoT5-3b|**0.4789**|**0.6440**|**0.3165**|**0.7705**|
|BM25 + Rocchio|0.3886|0.4720|0.2733|0.5894|
|BM25 + Rocchio + MonoBERT-large|0.4065|0.5320|0.2607|0.6976|
|BM25 + Rocchio + MonoT5-large|0.0921|0.0960|0.1807|0.1969|
|BM25 + Rocchio + MonoT5-3b|0.4186|0.5480|0.2883|0.6549|
|qld + Rocchio|0.3758|0.5000|0.2588|0.6760|
|qld + Rocchio + MonoBERT-large|0.4022|0.5160|0.2752|0.6940|
|qld + Rocchio + MonoT5-large|0.0728|0.0920|0.1883|0.1909|
|qld + Rocchio + MonoT5-3b|0.4283|0.5760|0.2944|0.6626|
|SBERT|0.3438|0.4400|0.1714|0.6183|
|SBERT + MonoBERT-large|0.4516|0.5960|0.2416|0.7444|
|SBERT + MonoT5-large|0.0854|0.0760|0.1531|0.1693|
|SBERT + MonoT5-3b|0.4305|0.5840|0.2518|0.7034|

Based on [pygaggle](https://github.com/castorini/pygaggle)