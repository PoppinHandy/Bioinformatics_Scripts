#Takes in a sequence file as input and outputs the reverse complement of the sequence

from Bio.Seq import Seq

f = raw_input("Welcome to the Reverse Complement tool! Enter your text file: ")

of = open(f, "r")
my_seq = Seq(of.read())

print my_seq.reverse_complement()
