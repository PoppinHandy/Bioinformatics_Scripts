#!usr/bin/python

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

final_file = open('/home/phamgouran/Browne_lab/Python_scripts/alignment_list_ED-I-5.out')
final_set = set()

for line in final_file:
	final_set.add(line)

#print "final_set obtained."
for entry in final_set:
	for final_record in SeqIO.parse("/home/phamgouran/Browne_lab/Walnut_reads/Walnut_filtered/FASTA/ED-I-5.notwalnutplastids.fas", "fasta"):
		if final_record.id == entry:
			print ">" + final_record.id
			print final_record.seq

 


