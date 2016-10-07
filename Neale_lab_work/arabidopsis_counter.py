#!/usr/bin/python
from __future__ import print_function, division
'''
Task:
Shows the use of counter, biopython's parse function
and prints the GC content of the arabidopsis chromosomes
'''
from collections import Counter
from Bio.Seq import Seq
from Bio import SeqIO
import glob
from Bio.Alphabet import IUPAC


c = Counter()
g = Counter()
m = Counter()
for fasta_file in glob.glob(r'/home/andy/DOC/neale_lab/Arabidopsis_thaliana/*.fas'):
	for record in SeqIO.parse(fasta_file, "fasta"):
		if record.id == 'mitochondria':
			m.update(str(record.seq))
		elif record.id == 'chloroplast':
			c.update(str(record.seq))
		else:
			g.update(str(record.seq))
print ('The mitochondria has ' +str(m))
print ('The cholorplast has ' + str(c))
print ('The chromosomes have ' + str(g))

print ('The total sum of mitochondria nucleotides is: ', str(sum(m.values())))
print ('The total sum of chloroplast nucleotides is: ', str(sum(c.values())))
print ('The total sum of chromosome nucleotides is: ', str(sum(g.values())))

m_GC = ((m['G'] + m['C'])/sum(m.values()))*100 
c_GC = ((c['G'] + c['C'])/sum(c.values()))*100 
g_GC = ((g['G'] + g['C'])/sum(g.values()))*100 

print('The GC content of mitochondria is: {:.2f}% '.format(m_GC))
print('The GC content of chloroplast is: {:.2f}% '.format(c_GC))
print('The GC content of chromosomes is: {:.2f}%'.format(g_GC))



