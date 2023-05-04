import os
import re
import json
from tqdm import tqdm

def get_json(): #for sparse retrieval
    with open("corpus/corpus.json", "w") as fw:
        for path, dirs, files in tqdm(os.walk("dataset")):
            #print(root, dirs, files)
            if len(files) == 0:
                continue
            for file in files:
                file_path = path + "/" + file
                with open(file_path, "r") as fin:
                    content = fin.read().strip()
                content = content.replace("\n", "").replace("\t", "").replace("\r", "").replace("&#xD;", " ").replace("&gt;", ">").replace("&lt;","<").replace("&amp;","&").replace("&quot;","\"").replace("&apos;","\'")
                content = re.findall(r"<textblock>.+?</textblock>", content)
                texts = "".join([text[11:-12] for text in content])
                texts = " ".join(texts.split())
                docid = file[:-4]
                json_str = json.dumps({'id' : docid, 'contents' : texts})
                fw.write(json_str + "\n")

def get_tsv(): #for dense retrieval
    with open("corpus/corpus.json", "r") as fin, open("corpus.tsv", 'w') as fout:
        for line in fin:
            line = json.loads(line)
            id, content = line['id'], line['contents']
            fout.write(id + "\t" + content + "\n")

get_json()          
get_tsv()