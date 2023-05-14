import matplotlib.pyplot as plt
import json
import matplotlib.cm as cm
import numpy as np

plt.figure(figsize=(8, 6))

res = []

with open('655PCY1D016-Alignment.json') as f:
    results = json.load(f)

for read in results['BlastOutput2']:
    read_name = read['report']['results']['search']['query_title']

    hits = [hit for hit in read['report']['results']['search']['hits'] if
            float(hit['hsps'][0]['bit_score']) >= 160]  # 181.623 for all

    if hits:
        top_hit = hits[0]['description'][0]['sciname']
        top_score = hits[0]['hsps'][0]['bit_score']
        scientific_name = top_hit.split('[')[-1].split(']')[0]
        res.append([read_name, scientific_name, top_score])

top_data = sorted(res, key=lambda x: x[2], reverse=True)

pie_data = sorted(res, key=lambda x: x[1])
print(res)

counts = {}
for item in pie_data:
    name = item[1]
    if name in counts:
        counts[name] += 1
    else:
        counts[name] = 1

labels = counts.keys()
sizes = counts.values()
labels = [label for label in labels]

num_labels = len(labels)

cmap = cm.get_cmap('tab20', num_labels + 9)
color_dict = {}
for i, label in enumerate(labels):
    color_dict[label] = cmap(i)


def autopct_fn(value):
    return f'{value:.1f}%'


sizes = counts.values()
colors = [color_dict[label] for label in labels]

colors = plt.cm.Set3.colors[:len(labels)]

myexplode = explode = [0.2 if label.startswith('Canis') or label.startswith('Felis') or label.startswith('Lynx') else 0
                       for label in labels]
wedgeprops = {'linewidth': 10, 'edgecolor': 'white'}

plt.pie(sizes, labels=labels, colors=colors, autopct=autopct_fn, explode=myexplode)
plt.axis('equal')
plt.savefig('pie_geq_160.png', dpi=800)
