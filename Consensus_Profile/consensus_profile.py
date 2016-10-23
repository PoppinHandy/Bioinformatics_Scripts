# Constructs a consensus string and profile matrix for a collection of DNA strings of equal length in FASTA format.
# Consensus string is the combination of the most common characters in the DNA strings at all positions of the string.

def profile_matrix(dna_strings, length):
	n_matrix = {"A": [], "G": [], "C": [], "T": []};
	
	# Created dictionary containing nucleotides as keys and lists of the frequency of the nucleotides as values
	# Initializing the values
	for init_count in range(0, length):
		for keys in n_matrix:
			n_matrix[keys].append(0);

	for dna_count in range (0, length):
		for char_count in range(0, length): 
			n_matrix[dna_strings[dna_count][char_count]][char_count] += 1

	print n_matrix

def main():
	
	f = raw_input("Enter the file name: ")
	fo = open (f, "r")


		
