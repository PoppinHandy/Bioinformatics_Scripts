
file = raw_input("Welcome to the Nucleotide Counter! Enter the name of the file: ")
nucleotide_file = open(file, 'r')

A = 0
C = 0
G = 0
T = 0
for line in nucleotide_file:
	for x in range(0, len(line) - 1):
		if line[x] == 'A':
	   		A += 1
		elif line[x] == 'G':
	   		G += 1
		elif line[x] == 'T':
			T += 1
		elif line[x] == 'C':
			C += 1
		else:
			print("A nucleotide was not recognized")

print A, C, G, T
	
    
