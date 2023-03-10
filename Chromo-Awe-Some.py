import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy import stats
import collections


human_ch21_FULL = open (r'C:\Users\Jenny\Desktop\Studium\1. Semester\GDBI files\HS_chromo21FULL.txt')
FULL_stored = human_ch21_FULL.read()
human_ch21_FULL.close()

#mouse_ch19_FULL = open (r'C:\Users\Jenny\Desktop\mus musculus chromosome 19.txt')
#FULL_stored = mouse_ch19_FULL.read()
#mouse_ch19_FULL.close()

#e_coli_FULL = open (r'C:\Users\Jenny\Desktop\Escherichia coli str. K-12 substr. MG1655 complete genome .txt')
#FULL_stored = e_coli_FULL.read()
#e_coli_FULL.close()

#sars_cov_2_FULL = open (r'C:\Users\Jenny\Desktop\SARS-CoV-2-wuhan-genome.txt')
#FULL_stored = sars_cov_2_FULL.read()
#sars_cov_2_FULL.close()

#d_radiodurans_ch1 = open (r'C:\Users\Jenny\Desktop\Deinococcus radiodurans strain R1 dM1 chromosome I.txt')
#FULL_stored = d_radiodurans_ch1.read()
#d_radiodurans_ch1.close()

#c_milii_mito = open (r'C:\Users\Jenny\Desktop\Callorhinchus milii mito.txt')
#FULL_stored = c_milii_mito.read()
#c_milii_mito.close()

nucleos =["A", "C", "G", "T"]
DNA_reverseComplement ={'A':'T','T':'A','G':'C','C':'G'}


def validateSeq(seq):
    seq = seq.upper()
    removeThis = ['N', 'R', 'M', '\n']
    for character in removeThis:
        seq = seq.replace(character,"")
    #for nuc in seq:
     #   if nuc not in nucleos:
      #      return print ("Sequence is INVALID"), print(dict(collections.Counter(seq)))
    return (print ("Sequence is VALID\n","\nSampling the beginning of Sequence: ", (seq [0:20])),
            print (                    "           ","Colored representation: ", colored(seq [0:20])),
            print (),
            print (                      "Sampling the end of Sequence:       ",seq [(len(seq)-20):len(seq)]),
            print (                    "           ","Colored representation: ", colored(seq [(len(seq)-20):len(seq)])),
            print (),
            print ("Nucleotide make-up:", 
            dict(collections.Counter(seq))),
            print (),
            print("Sequence length:", len(seq)))


def transcription (seq):
    removeThis = ['N', 'R', 'M', '\n']
    for character in removeThis:
        seq = seq.replace(character,"")
    for t in seq:
        RNAseq = seq.replace ("T","U")
        return (print ("Sampling the beginning of RNA-Sequence:", RNAseq [0:20]), 
                print (),
                print ("RNA-Nucleotide make-up:",
                dict(collections.Counter(RNAseq))))
    

def reverseComplement (seq):
    removeThis = ['N', 'R', 'M', '\n']
    for character in removeThis:
        seq = seq.replace(character,"")
    complement = "".join([DNA_reverseComplement [nuc] for nuc in seq])#[::-1]
    
    return print (complement [0:20])

 
def DNA (seq):
    removeThis = ['N', 'R', 'M', '\n']
    for character in removeThis:
        seq = seq.replace(character,"")
    
    return print (seq [0:20])

def SampleLength(seq):
    return len(seq [0:20])

def calcGcContent(seq, winSize=10):
    seq = seq.upper()
    removeThis = ['N', 'R', 'M', '\n']
    for character in removeThis:
        seq = seq.replace(character,"")
    gcValues = []
    for i in range(len(seq)-winSize):
        subSeq = seq[i:i+winSize]
        numGc = subSeq.count('G') + subSeq.count('C')
        value = numGc/float(winSize)
        gcValues.append(value)
    return gcValues

def gcContPercentage (seq):
    AT = 0
    GC = 0
    for base in seq:
        if base=="A" or base=="T":
            AT = AT+1
            # AT += 1
        elif base=="G" or base=="C":
            GC = GC+1
            # GC += 1

    GC_percentage = 100*float(GC)/float(GC+AT)
    two_decimals = round(GC_percentage, 2)
    #GC_percentage = 100.0*GC/GC+AT

    return print ("The GC content of the sequence via the function is:", (two_decimals), "%")

def colored(seq):
    bcolors = {
        'A': '\033[41m',
        'C': '\033[42m',
        'T': '\033[43m',
        'G': '\033[44m',
        'reset': '\033[0;0m'
    }

    tmpStr = ""
    dot =" "

    for nuc in seq:
        if nuc in bcolors:
            tmpStr += bcolors[nuc] + dot
        else:
            tmpStr += bcolors['reset'] + nuc

    return tmpStr + '\033[0;0m'

def count_k_mers (seq, k):
    
    k_freq = {}
    seq = seq.upper()
    removeThis = ['N', 'R', 'M', '\n']
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
    return k_freq
   
    
# RESULTS

print ("___________________________________________________________________________________________________")
print ()
print ("Full sequence analysis:")
print ("____________________________")
print ()
validateSeq(FULL_stored)
print ("___________________________________________________________________________________________________")
print ()
print ()
print ("DNA to RNA")
print ()
transcription(FULL_stored)
print ()
print ()
print ("___________________________________________________________________________________________________")
print ()
print ()
print ("DNA complement sample")
print ()
(DNA(FULL_stored))
print (f"{''.join(['|' for c in range(SampleLength(FULL_stored))])}")
reverseComplement(FULL_stored)
print ()
print ("___________________________________________________________________________________________________")
print ()
gcContPercentage(FULL_stored)
print ()
print ("___________________________________________________________________________________________________")
#print ("G-C ratio per 10 nucleotides:")
#print ()
#print (calcGcContent(FULL_stored))
print ()
print ("2-mers:")
print ()
print (count_k_mers(FULL_stored,2))
print ()
print ("3-mers")
print ()
print (count_k_mers(FULL_stored,3))
print ()
print ("___________________________________________________________________________________________________")



print ()
print ()
print ("END")
print ()
