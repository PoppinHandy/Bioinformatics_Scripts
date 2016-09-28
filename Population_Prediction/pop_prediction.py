# Population Prediction program that gives the amount of pairs of a species produced after a set number of months
# INPUT: months, amount of children produced per pair in a text file (ie. 5, 3 = 5 months and 3 pairs of children produced per pair)
# OUTPUT: number of pairs after the months projected
# Assumes starting pair is 1 and the pairs mature to reproductive age after one month


def total(t, init_month, end_month, children_amount):
	presentGen = 0
	prevGen = 0
	while init_month != end_month:
		if init_month == 0:
			presentGen = 1
			prevGen = 1 
			t.append(1)
			init_month = init_month + 1

		else:
			presentGen = children_amount * prevGen
			prevGen = t[init_month - 1]
			t.append(presentGen + prevGen)
			init_month = init_month + 1

	else:
		presentGen = children_amount * prevGen
		prevGen = t[init_month - 1]
		print presentGen + prevGen	
		
def main():
	filename = raw_input("Welcome to the population predictor! Enter the file: ")
	f = open(filename, "r")
	for line in f:
		parameters = line.strip().split(' ')
	months = int(parameters[0])
	children = int(parameters[1])
	
	# Storing all the month totals in a list for usage for future months
	t = list()
	total(t, 0, months - 2, children)

main()
	
