#!usr/bin/python

import subprocess
from subprocess import call


#retrieving file names
loc = '/home/phamgouran/Browne_lab/Walnut_reads/Walnut_filtered'
files = []
ret = subprocess.check_output(['ls', loc]).split('\n')

for entry in ret:
	if 'fq' in entry:
		files.append(entry)

#Running fastq_to_fasta 
for query in files:
	command = 'fastq_to_fasta -v -i /home/phamgouran/Browne_lab/Walnut_reads/Walnut_filtered/%s -o /home/phamgouran/Browne_lab/Walnut_reads/Walnut_filtered/FASTA/%s.fas' % (query, query)
	args = command.split()
	print "Running ", args
	return_code = subprocess.call(args)


