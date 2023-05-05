import os
import re
import json
from tqdm import tqdm

def get_json():
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

get_json()          