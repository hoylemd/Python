# Random integer generation program
# generates a list of 25 integers between -100 and 100

import random
import math

list_length = 25
lower_bound = -100
upper_bound = 100
list_range = upper_bound - lower_bound

# seed the random number generator
random.seed()

range(10)

# generate the random ints
for i in range(25):
	print math.floor((random.random() * list_range) - lower_bound)