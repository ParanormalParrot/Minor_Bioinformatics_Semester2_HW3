import json
import matplotlib.pyplot as plt
import numpy as np

seq = 'TCTACGCTTCTCCACAAATAATATACATCTAATAGCAAAACCTTTTACCTGCATATCATGAGGCTGGCTACTATCTTGCCTATGCCAAAGGAATATTATG' # fragment 77


with open('fragments.fasta', 'w') as outfile:
    for i in range(len(seq), 0, -1):
        fragment = seq[:i]
        record = f'>fragment_{i}\n{fragment}\n'
        outfile.write(record)