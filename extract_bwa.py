#!/usr/bin/python

alignment_file = open('/home/phamgouran/Browne_lab/Walnut_reads/Walnut_raw_reads/Project_GBHG_L2_HiSeq134P_Gouran/alignments/ED-I-3_hinds_align_header_removed.out')

for line in alignment_file:
	col = line.rsplit("\t")
	if (int(col[4]) > 0):
		#print col[4] + "\n"
		print ">" + col[0] + "\n" + col[9]
alignment_file.close()
