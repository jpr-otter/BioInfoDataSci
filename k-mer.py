import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy import stats
import collections

human_ch21_FULL = open (r'C:\Users\Jenny\Desktop\HS_chromo21FULL.txt')
human_FULL_stored = human_ch21_FULL.read()
human_ch21_FULL.close()

mouse_ch19_FULL = open (r'C:\Users\Jenny\Desktop\mus musculus chromosome 19.txt')
mouse_FULL_stored = mouse_ch19_FULL.read()
mouse_ch19_FULL.close()

e_coli_FULL = open (r'C:\Users\Jenny\Desktop\Escherichia coli str. K-12 substr. MG1655 complete genome .txt')
coli_FULL_stored = e_coli_FULL.read()
e_coli_FULL.close()

sars_cov_2_FULL = open (r'C:\Users\Jenny\Desktop\SARS-CoV-2-wuhan-genome.txt')
cov_FULL_stored = sars_cov_2_FULL.read()
sars_cov_2_FULL.close()

d_radiodurans_ch1 = open (r'C:\Users\Jenny\Desktop\Deinococcus radiodurans strain R1 dM1 chromosome I.txt')
radio_FULL_stored = d_radiodurans_ch1.read()
d_radiodurans_ch1.close()

c_milii_mito = open (r'C:\Users\Jenny\Desktop\Callorhinchus milii mito.txt')
shark_FULL_stored = c_milii_mito.read()
c_milii_mito.close()


def count_k_mers (seq, k):
    
    k_freq = {}
    seq = seq.upper()
    removeThis = ['N', 'R', 'M', 'Y', '\n']
    for character in removeThis:
        seq = seq.replace(character,"")
    for i in range (0, len(seq) - k + 1):
        kmer = seq [i:i + k]
        if kmer in k_freq:
            k_freq[kmer] += 1
        else:
            k_freq[kmer] = 1
    k_freq = k_freq.items()
    k_freq = sorted (k_freq)
    return k_freq, len(k_freq)


print ()
print ()
print ("___________________________________________________________________________________________________")
print ()
print ("HUMAN")
print ()
print (count_k_mers(human_FULL_stored,3))
print ("___________________________________________________________________________________________________")
print ()
print ("MOUSE")
print ()
print (count_k_mers(mouse_FULL_stored,3))
print ("___________________________________________________________________________________________________")
print ()
print ("COLI")
print ()
print (count_k_mers(coli_FULL_stored,3))
print ("___________________________________________________________________________________________________")
print ()
print ("COV")
print ()
print (count_k_mers(cov_FULL_stored,3))
print ("___________________________________________________________________________________________________")
print ()
print ("RADIO")
print ()
print (count_k_mers(radio_FULL_stored,3))
print ("___________________________________________________________________________________________________")
print ()
print ("SHARK")
print ()
print (count_k_mers(shark_FULL_stored,3))
print ("___________________________________________________________________________________________________")
