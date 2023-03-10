import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy import stats
import collections


# test string

randoDNA = "ATTGCGCGATA"

# opens DNAseq file, turns in into a variable, closes files again


human_ch21_FULL = open (r'C:\Users\Jenny\Desktop\HS_chromo21FULL.txt')
FULL_stored = human_ch21_FULL.read()
human_ch21_FULL.close()




# check if DNAseq is valid, meaning only ATCG, also turns all letter to uppercase

nucleos =["A", "C", "G", "T"]

def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in nucleos:
            return print ("Seq is INVALID")
    return print ("Seq is valid", tmpseq)

# creates dictionary for nucleotides and pain-in-da-butt-other-letters
"""
def countNucFrequency (seq):
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0, "\n": 0, "N": 0, "M": 0, "R": 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict
"""

# get rid of all the letters that are not ATCG
# creates dictionary via collections, same as above but shorter in code


def deleteNonNucleos (seq):
    removeThis = ['N', 'R', 'M', '\n']
    for character in removeThis:
        seq = seq.replace(character,"")
    
    return print (dict(collections.Counter(seq))), print ("Seq length:", len(seq))



# turn DNA strand into the cDNA and then transcribe it into RNA
# translate RNA into Polypeptide

# transcription

def transcription (seq):
    for t in seq:
        seq = seq.replace ("T","U")
        return print (dict(collections.Counter(seq)))
    
def valiDeleTrans (seq):
    tmpseq = seq.upper()
    for nuc in tmpseq:
            removeThis = ['N', 'R', 'M', '\n']
            for character in removeThis:
                seq = seq.replace(character,"")
                seq = seq.replace ("T","U")
     
            print (seq[0:20])
            print ()
            
    return print("First 20 nucleos:\n"),print (seq[0:20]), 
            print (dict(collections.Counter(seq))), 
            print ("Seq length:", len(seq))
    
    

    
    


# display of results

print ("_______________________________________________________________")
print ()
print ("Testcase DNAseq randoDNA: ")
print (validateSeq(randoDNA))
#print (countNucFrequency(randoDNA))
print ("_______________________________________________________________")
print ()
print ()
print ("_______________________________________________________________")
print ()
print ("DNAseq from file HS chromo21 FULL: " )
print ()
print (validateSeq(FULL_stored))
print ()
print ()
print ("Nucleotide proportions in the DNAseq from file")
print ()
#print (countNucFrequency(FULL_stored))
print ("_______________________________________________________________")
print ()
print ()
print ("_______________________________________________________________")
print ()
print ()
print ("_______________________________________________________________")
print ()
print ("Hopefully all non-Nucleo-letters were deleted")
print ()
print (deleteNonNucleos (FULL_stored))
print ()
print ("_______________________________________________________________")
print ()
print ("Transcribe DNA into RNA: the test seq")
print ("compare the seqs")
print ()
print ("test seq", randoDNA)
print ("into RNA", transcription(randoDNA))
print ()
print ()
print ("the whole chromosome: ")
print (transcription(FULL_stored))
print ()
print (dict(collections.Counter(FULL_stored)))
print ("_______________________________________________________________")
print ()
print ()
print ("All in one function: ")
print ()
print (valiDeleTrans(FULL_stored))
print ("_______________________________________________________________")
print ()
print (FULL_stored[0:20])




# die frage bleibt, wie sieht die verteilung der nicht-nukleotid buchstaben aus
#

# create the dataframe

data_frame = pd.read_csv(r'C:\Users\Jenny\Desktop\HS_chromo21FULL.txt', delimiter = "\t")
