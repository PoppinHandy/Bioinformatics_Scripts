# Script to take in a RNA sequence and turn it into protein

def main():

	f = raw_input("Enter a file with RNA sequence: ")
	fi = open(f, "r")

	RNA_codon = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG":"L",
			"UCU": "S", "UCC":"S", "UCA": "S", "UCG": "S",
			"UAU": "Y", "UAC": "Y", "UAA": "", "UAG": "",
			"UGU": "C", "UGC": "C", "UGA": "", "UGG": "W",
			"CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L", 
			"CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
			"CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q", 
			"CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
			"AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
			"ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
			"AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
			"AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
			"GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
			"GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A", 
			"GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
			"GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

	line = fi.readline().rstrip()
	
	protein = ""
	for x in range(0, len(line), 3):
		codon = line[x:x+3]
		protein += RNA_codon[codon]

	print protein
main()
