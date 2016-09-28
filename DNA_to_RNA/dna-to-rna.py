#Translates DNA to RNA given a text file of nucleotide sequences


file = raw_input("Welcome to the DNA to RNA translation tool! Enter the name of the text file you wish to translate: ")

of = open(file, "r")

rna = ""
for line in of:
	rna = line.replace('T', 'U')
print rna

