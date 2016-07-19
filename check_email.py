#!usr/bin/python

import smtplib

FROM = 'brownelab94@gmail.com'
TO = 'apham@ucdavis.edu'
user = 'brownelab94'
password = '****'

msg = "Brownelab mail completed!"
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(user, password)
server.sendmail(FROM, TO, msg)
server.quit()

