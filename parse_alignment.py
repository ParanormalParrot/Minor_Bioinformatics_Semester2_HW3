from Bio import Entrez, SeqIO
import random
import json
import numpy as np

res = []

with open('Alignment1.json') as f:
        results = json.load(f)

for read in results['BlastOutput2']:
    read_name = read['report']['results']['search']['query_title']


    hits = [hit for hit in read['report']['results']['search']['hits']]

    if hits:
        top_identity = hits[0]['hsps'][0]['identity']

        res.append(top_identity)

print(res)
print(np.mean(res))