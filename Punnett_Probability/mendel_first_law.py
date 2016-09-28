# Program that reads 3 numbers each representing individuals for homozygous dominant, heterozygous, and homozygous recessive, respectively and outputting the probaility that two randomly selected organisms will produce an individual with a dominant allele

from __future__ import division

f = raw_input("Enter the file: ")

of = open(f, "r")

l = of.readlines(1)

organisms = l[0].rstrip().split(" ")
r = int(organisms[2])
hd = int(organisms[0])
h = int(organisms[1])
total = r + hd + h 

# Strategy is to find the probability that an individual will produce a recessive allele and subtract that from 1

# Recessive x Recessive
r_r = (r/total)*(r - 1)/(total - 1)

# Heterozygous x Recessive
h_r =(1/2)*((r/total)*(h/(total - 1)) + (h/total)*(r/(total - 1)))

# Heterozygous x Heterozygous
h_h = (h/total)*((h - 1)/(total - 1))*(1/4)

#Total Probability

prob = 1 - (r_r + h_r + h_h)

print prob 
