from Bio import Entrez, SeqIO
import random
import json
import numpy as np

chr_id = "CM000686"
Entrez.email = ""

handle = Entrez.efetch(db="nucleotide", id=chr_id, rettype="fasta", retmode="text")
record = SeqIO.read(handle, "fasta")

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
