import collections

LINE_1_gene = ('GAA GTT GAA AAC TTT GAA AAA AAT TTA GAA GAA TGT ATA ACT AGA ATA ACC AAT ACA GAG AAG TGC TTA AAG GAG CTG ATG GAG CTG AAA ACC AAG GCT CGA GAA CTA CGT GAA GAA TGC AGA AGC CTC AGG AGC CGA TGC GAT CAA CTG GAA GAA AGG GTA')
LINE_1_protein =  ('EVENFEKNLEECITRITNTEKCLKELMELKTKARELREECRSLRSRCDQLEERV')
LINE_1_protein

print ("Length of the complete nucleotide-string with spaces in between:", len(LINE_1_gene)) 
stop_codon = LINE_1_gene.find ("TAA")  

print ()
print ("ATG start codon at position --", LINE_1_gene.find("ATG", 0, 215), "-- in the nucleotide-string")
print ("AAA start codon at position --", LINE_1_gene.find("AAA"), "-- in the nucleotide-string")

print ()
if stop_codon < 0:
    print ("No TAA stop codon, hinting at open reading frame")
else:
    print ("TAA stop codon at position --", LINE_1_gene.find("TAA"), "-- in the nucleotide-string" )

print ()
print ("How many amino acids:", len(LINE_1_protein))
print ()
print ("Distribution of amino acids:\n\n", dict (collections.Counter(LINE_1_protein)))
print ()

teststring = ("abc")
teststring.find("a")
teststring.find("b")
teststringTWO = ("a bc")
print (teststringTWO.find("b"))
