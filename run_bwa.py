#!usr/bin/python

import smtplib
import subprocess
from subprocess import call

FROM = 'brownelab94@gmail.com'
TO = 'apham@ucdavis.edu'
user = 'brownelab94'
password = 'megawish'

#retrieving file names
loc = '/home/phamgouran/Browne_lab/Walnut_reads/Walnut_filtered'
files = []
ret = subprocess.check_output(['ls', loc]).split('\n')

for entry in ret:
	if 'fq' in entry:
		files.append(entry)

#Running bwa aln
for query in files:
	command = 'bwa aln -n 0.01 -t 2 asm.scafSeq /home/phamgouran/Browne_lab/Walnut_reads/Walnut_filtered/%s ~/Browne_lab/Walnut_reads/Hinds_walnut/%s.sai' % (query, query)
	args = command.split()
	print "Running ", args
	return_code = subprocess.call(args)


	if (return_code == 0):
		msg = query, " completed!"
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.starttls()
		server.login(user, password)
		server.sendmail(FROM, TO, msg)
		server.quit()

