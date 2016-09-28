# Script that takes in two DNA strings of equal length and outputs the Hamming Distance, aka the number of mismatches between the two strings.

import re

f = raw_input("Enter the name of the file (must have 2 DNA strings): ")

of = open(f, "r")

lines = of.readlines()

mismatches = 0
char1 = []
char2 = []

for c in lines[0]:
	char1.append(c)	

for c2 in lines[1]:
	char2.append(c2)

for x in range(0, len(char1) - 1):
	if char1[x] is not char2[x]:
		mismatches += 1

print mismatches
	
