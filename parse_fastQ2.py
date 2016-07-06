#!usr/bin/python

fo = open ('/home/phamgouran/Browne_lab/Walnut_reads/Walnut_filtered/ED-I.notwalnutplastids.fq', 'r')
ID_list = []
for line in fo:
    #print "Reading: %s" % line
    list_of_words = line.split()
    if "HWI" in list_of_words[0].rsplit("+")[0]:
    	print list_of_words[0].rsplit("+")[0].rsplit("@")[1].rsplit("/")[0]
    	#ID_list.append(list_of_words[0].rsplit("+")[0].rsplit("@")[1])

print ID_list
fo.close()

