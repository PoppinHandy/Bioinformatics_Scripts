#!usr/bin/python

from __future__ import print_function, division
from BCBio import GFF
import gffutils
import glob
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq


db = gffutils.FeatureDB("/home/andy/UCD/LAB/neale_lab/DOC/Arabidopsis_thaliana_ORG/TAIR10_db.db", keep_order=True)
chr_seq = dict()
fasta_filepath = "/home/andy/UCD/LAB/neale_lab/DOC/Arabidopsis_thaliana_ORG/TAIR10_organellar/*.fas"

"""
Task:
Outputs a fasta representation of the sequence read in by gffutils
>>> ARGS:       record of sequence, sequence id of record, and description of sequence 
>>> RETURN:     none
"""
def seq_to_fasta(seq, seq_id, descrip):
	input_seq = Seq(str(seq))
	seq_record = SeqRecord(input_seq, id=str(seq_id))
	seq_record.description = str(descrip)
	print (seq_record.format("fasta"))

"""
Task:
Dictionary created for sequence pulling from fasta files. 
Program asks what feature to look for.
Gffutil database used to parse through gff3 file for 
particular feature and sequence pulled from dict for
that feature. It then uses function seq_to_fasta to
print out in fasta format.
>>> ARGS: gff3 file 
>>> RETURN: None    
"""
def main():
	for fasta_file in glob.glob(fasta_filepath):
		for seq_record in SeqIO.parse(fasta_file, 'fasta'):
			chr_seq[seq_record.id] = seq_record.seq
#	type_of_feature = raw_input("What type of feature do you want to print out? ")

	featuretype_iterator = db.features_of_type("protein")
	for rec in featuretype_iterator:
		for x in chr_seq:
			if (rec.seqid == 'ChrC' and x == 'chloroplast') or (rec.seqid == 'ChrM' and x == 'mitochondria'):
				sequence_id = rec.id
				seq_source = rec.seqid

				if rec.strand == '-':
					if rec.frame == '.':
						coding_frame = 0
					else:
						coding_frame = int(rec.frame)
					mrna_seq = chr_seq[x][rec.start-1:rec.end-coding_frame]				
					mrna_seq = mrna_seq.reverse_complement()
					seq_to_fasta(mrna_seq, sequence_id, seq_source)

				elif rec.strand == '+':
					if rec.frame == '.':
						coding_frame = 0
					else:
						coding_frame = int(rec.frame)
					mrna_seq = chr_seq[x][rec.start-1+coding_frame:rec.end]				
					seq_to_fasta(mrna_seq, sequence_id, seq_source)
main()
