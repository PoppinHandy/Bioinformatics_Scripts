# Constructs a consensus string and profile matrix for a collection of DNA strings of equal length in FASTA format.
# Consensus string is the combination of the most common characters in the DNA strings at all positions of the string.

# Takes as input an array containing dna sequences as well as the common lengths 
# and outputs a dictionary of the frequencies of nucleotides

def profile_matrix(dna_strings, length):
	n_matrix = {"A": [], "C": [], "T": [], "G": []};
	
	# Created dictionary containing nucleotides as keys and lists of the frequency of the nucleotides as values
	# Initializing the values
	for init_count in range(0, length):
		for keys in n_matrix:
			n_matrix[keys].append(0);

	for dna_count in range (0, len(dna_strings)):
		for char_count in range(0, length): 
			n_matrix[dna_strings[dna_count][char_count]][char_count] += 1

	# Display the profile matrix
	for keys in n_matrix:
		# Turning the values into strings for clear printing	
		clean_matrix = " ".join(str(e) for e in n_matrix[keys])
		print "%s: %s" % (keys, clean_matrix)

	return n_matrix
	
# Takes a dictionary as input and 
# prints the most homologous dna sequence based on the dictionary

def displayConsensusString(prof_matrix, length):

	dnaConsensus = ""
	temp = ""
	maxNucleotide = 0 
	for dna_count in range(0, length):
		for key in prof_matrix:
			if (prof_matrix[key][dna_count] > maxNucleotide): 
				maxNucleotide = prof_matrix[key][dna_count]
				temp = key
		dnaConsensus += temp
		temp = ""
		maxNucleotide = 0			

	print dnaConsensus	
		
def main():
	
	f = raw_input("Enter the file name: ")
	fo = open (f, "r")
	
	dna_arr = []
	
	# Reading in the FASTA file and storing sequences in an array
	for line in fo:
		if ">" in line:
			dna_arr.append(fo.next().rstrip())

	dna_length = len(dna_arr[0]) 
	displayConsensusString(profile_matrix(dna_arr, dna_length), dna_length)
		
main()	

		
