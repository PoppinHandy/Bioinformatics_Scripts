#!/usr/bin/python

"""
// -----------------------------------------------------------------------------
// UC DAVIS
// apham@ucdavis.edu
//
// $Author: andy $
// $Date: 2014/09/24 22:48:36 $
// $RCSfile: translate_data.py,v $
// $Revision: 1.4 $
// Description:
//	This program parses through a gff3 file and searches for the mRNA
//	of a chromosome, and matches it to its corresponding CDS.
//	It then takes the CDS region and outputs the sequence of 
//	that CDS region. It displays the sequence id, the ID of the CDS
//	and the sequence of the CDS.
// -----------------------------------------------------------------------------
//
// REVISION HISTORY:
//
// $Log: translate_data.py,v $
// Revision 1.4  2014/09/24 22:48:36  andy
// Added to comments
//
// Revision 1.3  2014/09/22 21:59:49  andy
// Deleted translate_sequence function and cleaned up code
//
// Revision 1.2  2014/09/21 06:38:11  andy
// Added write to file and protein translation
//
// Revision 1.1  2014/09/20 23:22:24  andy
// first pass version
//
//
// -----------------------------------------------------------------------------
"""

from __future__ import print_function, division
from Bio import SeqIO
import glob
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

chr_seq = dict()
cds_data = dict()

class cds_region:
	"""Class to store ID and Sequence
	"""
	def __init__(self):
		self.id = ''
		self.seq = ''

"""
Task:
Uses glob to read all the .fas files
Parse each fasta file to get id and seq
and create dictionary named chr_seq with key is id and value is seq
Makes another dictionary named chromosome_dict with the same
keys as chr_seq, but pointing to a list

>>> ARGS: 	name of fasta files to read (.fas) 
>>> RETURN: 	none
"""
def open_fastafile(fasta_filepath):
	global chr_seq
	global cds_data 
	#Making the sequence dictionary
	for fasta_file in glob.glob(fasta_filepath):
		for seq_record in SeqIO.parse(fasta_file, 'fasta'):
			if seq_record.id not in ('Chr1', 'Chr2', 'Chr3', 'Chr4', 'Chr5'): continue
			chr_seq[seq_record.id] = seq_record.seq

	cds_data = dict.fromkeys(chr_seq, None)

"""
Task:
Opens the targeted gff3 file, and gets the sequence id from it.
If flag is not equal to 1, find an mRNA and store its sequence ID
and ID. If flag is 1 find the cds region with same IDs as mRNA and 
recover the sequence. Store the sequence in a dictionary with the
sequence ID as the key and a cds_region object as the value in a list.
>>> ARGS: gff3 file 
>>> RETURN: None	
"""
def gff3_parse(gff3_filepath):
	global cds_data
	flag = 0
	mrna_id = ''
	mrna_seqID = ''
	#Open gff3 file and extract contents
	for gline in open(gff3_filepath):
		gline = gline.rstrip('\n')
		split_line = gline.strip().split('\t')
		seq_id = split_line[0]

		#Don't want chromosomes or mitochondrion
		if seq_id not in ('Chr1', 'Chr2', 'Chr3', 'Chr4', 'Chr5'): continue
		if flag == 1:
			if split_line[2] == 'CDS' and mrna_id == split_line[8].split(',')[0].split('=')[-1] and mrna_seqID == seq_id:	
				cds_parentID = split_line[8].split(',')[0].split('=')[-1]
				cds_start = int(split_line[3])
				cds_end = int(split_line[4])
				cds_seq = chr_seq[seq_id][cds_start-1:cds_end]
				if type(cds_data[seq_id]) != list:
					cds_data[seq_id] = list()
					c = cds_region()
					c.id = cds_parentID
					c.seq = cds_seq
					cds_data[seq_id].append(c) 		
				else:
					c = cds_region()
					c.id = cds_parentID
					c.seq = cds_seq
					cds_data[seq_id].append(c) 		
				flag = 0
		elif split_line[2] == 'mRNA': 
			mrna_id = split_line[8].split(';')[0].split('=')[-1]  
			mrna_seqID = seq_id	
			flag = 1

"""
Task:
Prints the selected output into two files, one for protein translation and normal sequence 
>>> ARGS: none
>>> RETURN: none
"""
def printToFile():
	seq_file = open("cds_sequence.txt", "w")
	protein_file = open("protein.txt", "w")
	seq_lines ="ID:"+ "\t"+ "ID NUM:"+ "\t\t"+ "Sequence" + "\n" 
	seq_file.write(seq_lines)
	protein_file.write("ID:"+ "\t"+ "ID NUM:"+ "\t\t"+ "Sequence:" + "\n")
	for x in cds_data:
		for y in cds_data[x]:
			seq_lines = str(x + "\t"+ y.id +"\t" + y.seq + "\n")
			seq_file.write(seq_lines)
			protein_lines = str(x + "\t" + y.id + "\t" + y.seq.translate()+ "\n")
			protein_file.write(protein_lines)
	seq_file.close()
	protein_file.close()

"""
Task:
Calls all of the functions listed above
>>> ARGS: none 	 
>>> RETURN: none	
"""
def main():
	fasta_file = '/home/andy/UCD/LAB/neale_lab/DOC/Arabidopsis_thaliana_ORG/*.fas'
	open_fastafile(fasta_file)
	gff3_file = '/home/andy/UCD/LAB/neale_lab/DOC/Arabidopsis_thaliana_ORG/gff3_arth_just_forward_no_intron_genes.gff3'
	gff3_parse(gff3_file)
	printToFile()
main()
