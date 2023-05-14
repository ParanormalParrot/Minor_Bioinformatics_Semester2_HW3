from Bio import Entrez, SeqIO
import random
import json
import numpy as np

Entrez.email = ""

# выбираем хромосому на странице https://www.ncbi.nlm.nih.gov/assembly/GCF_000001405.40
chr_id = "CM000686"  # хромосома Y

handle = Entrez.efetch(db="nucleotide", id=chr_id, rettype="fasta", retmode="text")
record = SeqIO.read(handle, "fasta")
# выбираем случайную позицию и извлекаем фрагмент длиной 100
i = 0
while i < 100:
    start = random.randint(0, len(record.seq) - 100)
    end = start + 100
    fragment = record.seq[start:end]
    if 'N' in fragment:
        continue
    else:
        print(">fragment_" + str(i + 1))
        print(fragment)
        i += 1
