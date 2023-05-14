import json
import matplotlib.pyplot as plt
import numpy as np

with open('Alignment_2_human.json') as f:
    results = json.load(f)


def geq(arr, threshold):
    for i, val in enumerate(arr):
        if val > threshold:
            return i
    return -1


n_values = []
e_values = []
N_ = []

for read in results['BlastOutput2']:
    read_name = read['report']['results']['search']['query_title']
    try:
        first_score = float(read['report']['results']['search']['hits'][0]['hsps'][0]['identity'])
    except:
        first_score = None
    hits = [
        hit for hit in read['report']['results']['search']['hits'] if
        float(hit['hsps'][0]['identity']) == first_score
    ]  # 0 for all
    if hits:
        evalue = float(hits[0]['hsps'][0]['evalue'])
        e_values.append(evalue)

        n_values.append(read['report']['results']['search']['query_len'])
        N_.append(len(hits))
print(n_values)
print(n_values[geq(e_values, 0.05)])

plt.figure(figsize=(8, 6))
plt.plot(n_values, -1.0 * np.log10(e_values))
plt.xlim(max(n_values), min(n_values))
plt.xlabel('$n$')
plt.ylabel('$-lg(E)$')
plt.savefig('e_value_n.png', dpi=800)

plt.figure(figsize=(8, 6))
plt.plot(n_values[:-3], N_[:-3])
plt.xlim(max(n_values), min(n_values))
plt.xlabel('$n$')
plt.ylabel('$max ~ N$')
plt.savefig('max_N_n.png', dpi=800)
