#!usr/bin/python

alignment_file = open('/home/phamgouran/Browne_lab/Walnut_reads/Walnut_filtered/FASTA/BWA_INDEX/bwa_alignments_no_header.out', 'r')
fo = open ('/home/phamgouran/Browne_lab/Walnut_reads/Walnut_filtered/ED-I.notwalnutplastids.fq', 'r')
ID_list = []
for line in alignment_file:
    #print "Reading: %s" % line
    list_of_words = line.split()

    #print list_of_words[0]
    ID_list.append(list_of_words[0])

ID_set = set(ID_list)
alignment_file.close()

OG_list = [] 
for line2 in fo:
    #print "Reading: %s" % line
    list_of_words2 = line2.split()
    if "HWI" in list_of_words2[0].rsplit("+")[0]:
        #print list_of_words[0].rsplit("+")[0].rsplit("@")[1]
        OG_list.append(list_of_words2[0].rsplit("+")[0].rsplit("@")[1].rsplit("/")[0])

OG_set = set(OG_list)
fo.close()

final_list = ID_set - OG_set
print "ID_SET LENGTH: ", len(ID_set)
print "OG_SET LENGTH: ", len(OG_set)
print len(final_list)
print final_list
