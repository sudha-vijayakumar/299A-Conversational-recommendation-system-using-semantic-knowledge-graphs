#!/usr/bin/env python
# encoding: utf-8
import json
import random
import pandas as pd

#file generated by: /Users/sudhavijayakumar/Documents/299/299A-SMARTRec/QA DataScrappers/Get_AirbnbData.ipynb
df = pd.read_json('/Users/sudhavijayakumar/Documents/FAQ/data/nlu/faq.json',orient='records')

nlu_yml_file = open('/Users/sudhavijayakumar/Documents/FAQ/data/nlu.yml', 'a')
nlu_yml_file.write('\n\n- intent: faq')
nlu_yml_file.write('\n  examples: |')

for ind in df.index:
     print(df['a'][ind], df['q'][ind])
     nlu_yml_file.write('\n    - '+(df['q'][ind]).replace('-',' '))

nlu_yml_file.close()

# data = json.load(open("./faq.json", encoding="utf-8"))
# random.shuffle(data)
# data = data[:1000]
# for index, each in enumerate(data):
#     data[index]['index'] = index
# qs = [each['q'] for each in data]
# json.dump(data, open("faq.json", "wt", encoding="utf-8"), ensure_ascii=False, indent=4)
# with open("faq.md", "wt", encoding="utf-8") as f:
#     f.write("## intent:faq\n")
#     for q in qs:
#         f.write(f"- {q}\n")



