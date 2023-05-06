# TREC-2022-Clinical-Trials-Track
*Yiteng Tu*

### Requirements
```
python==3.9.12
tensorflow==2.7.0
pytorch==1.10.1+cuda11.1
cudatoolkit==11.1.1
transformers==4.21.3
faiss-gpu==1.7.2
pyserini==0.21.0
pygaggle==0.0.3.1
```

### Results
|  | NDCG@10 | P@10 | RPrec | MRR |
| :-----------: | :-----------: | :-----------: | :-----------: | :-----------: |
|Official Best Run|0.6125|0.5080|0.3297|0.7262|
|My Best Run w/o fusion|0.4789|0.5920|0.3165|0.7705|
|My Best Run Rank w/o fusion|5th|1st|2nd|1st|
|My Best Run w/ fusion|0.5242|0.6340|0.3447|0.8475|
|My Best Run Rank w/ fusion|3rd|1st|1st|1st|