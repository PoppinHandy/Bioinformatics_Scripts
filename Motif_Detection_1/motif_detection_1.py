# Script to make a very basic DNA motif detector
# INPUT: DNA sequence string followed by motif DNA sequence on next line in a separate file
# OUTPUT: Positions in the sequence where the motif occurs

def main():

	f = raw_input("Enter the file name: ")
	
	fi = open(f, "r")

	read = fi.readlines(0);
	sequence = read[0].rstrip();
	motif = read[1].rstrip();

	# Algorithm is to find position of the first substring that matches, cut the string up to the position of the substring match + 1 and repeat

	# Keep track of the position change when moving up the sequence
	temp_offset = 0

	# Keep track of the actual position since cutting up the substring resets the offset to 0
	actual_offset = temp_offset
	while motif in sequence:
		motif_pos = sequence.find(motif)
		print "%d"  % (motif_pos + 1 + actual_offset)
		temp_offset = motif_pos + 1
		actual_offset += temp_offset
		sequence = sequence[temp_offset:len(sequence)]
main()
