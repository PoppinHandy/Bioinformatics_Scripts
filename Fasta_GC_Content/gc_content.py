# This program is designed to read in a fasta file and output the sequence with the highest GC content

from __future__ import division
f = raw_input("Enter the name of the fasta file: ")
of = open(f, "r")

GC_content = dict()
gene_id = ""
sequence = ""

for line in of:
	line = line.rstrip()
	if ">" in line: 
		gene_id = line.split(">")[1]
		GC_content[gene_id] = "NULL" 
		sequence = ""
	else:
		sequence += line
		GC_content[gene_id] = sequence

highest_gc = 0.00
gc_id = "" 

for keys in GC_content:
	current_gc = (GC_content[keys].count("G") + GC_content[keys].count("C"))/(len(GC_content[keys]))	
	if current_gc > highest_gc:
		highest_gc = current_gc
		gc_id = keys

print "The ID with the higest GC content is:", gc_id, "with", highest_gc * 100, "%"
		
