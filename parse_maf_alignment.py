#!usr/bin/python
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

alignment_file = open('/home/phamgouran/Browne_lab/Walnut_reads/Walnut_filtered/FASTA/JE_alignments/JE-5_alns.maf')

ID_set = set()
query_set = set()

for line in alignment_file:
	if 's' in line:
		sequence = line.split()
		if sequence[0] == 's':
			ID_set.add(sequence[1])
alignment_file.close()

for seq_record in SeqIO.parse("/home/phamgouran/Browne_lab/Walnut_reads/Walnut_filtered/FASTA/JE-I-5.notwalnutplastids.fas", "fasta"):
	query_set.add(seq_record.id)

#print "query set finished."
my_records = []
final_set = query_set - ID_set
for record in final_set:
	print record


