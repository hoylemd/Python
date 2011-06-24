# Random integer generation module
# generates a list of integers between specified boundaries

import random
import math
import sys

def isNumeric(number):
	try:
		float(number)
		return True
	except ValueError:
		return False

# function to generate a list of <num_numbers> integers between 
## <lower> and <upper> inclusive.
def generateInts(num_numbers, lower, upper):
	# calculate the range
	list_range = upper - lower

	# seed the random number generator
	random.seed()

	#initialize the list
	new_list = list()

	# generate the random ints
	for i in range(num_numbers):
		newNumber = int(math.floor((random.random() * list_range) 
		 + lower))
		new_list.append(newNumber)
		
	return new_list