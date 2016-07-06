#!usr/bin/python

import smtplib
import subprocess
from subprocess import call

FROM = 'apham@ucdavis.edu'
TO = 'apham@ucdavis.edu'
user = 'apham'
password = 'evergreen_class_of_2012'
infected = '/home/phamgouran/Browne_lab/Walnut_reads/Walnut_filtered/ED-I-1.notwalnutplastids.fq'
noninfected = '/home/phamgouran/Browne_lab/Walnut_reads/Walnut_filtered/ED-N-1.notwalnutplastids.fq'
output = '/home/phamgouran/Browne_lab/Walnut_reads/Walnut_filtered/blastn_output_ED-I-1.out'
return_code = subprocess.call('blastn -subject %s -query %s -out %s' % (noninfected, infected, output))
if (return_code == 0):
	msg = "Blastn completed!"
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(user, password)
	server.sendmail(FROM, TO, msg)
	server.quit()

