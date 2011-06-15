# Random integer generation program
# generates a list of 25 integers between -100 and 100

import random
import math
import sys

# load default settings
list_length = 25
lower_bound = -100
upper_bound = 100

# parse arguments
argc = len(sys.argv)
if argc > 1:
	filename = sys.argv[1]
else:
	print "No output file provided. List will not be saved."
	filename = ""
	
if argc > 2:
	if sys.argv[0].isdigit():
		list_length = int(sys.argv[2])
	else:
		print "List length invalid, defaulting to 25"
		
if argc > 3:
	if sys.argv[0].isdigit():
		lower_bound = int(sys.argv[3])
	else:
		print "Lower bound invalid, defaulting to -100"
		
if argc > 4:
	if sys.argv[0].isdigit():
		upper_bound = int(sys.argv[3])
	else:
		print "Upper bound invalid, defaulting to 100"


list_length = 25
lower_bound = -100
upper_bound = 100
list_range = upper_bound - lower_bound

# seed the random number generator
random.seed()

#initialize the list
random_list = list()

# generate the random ints
for i in range(25):
	newNumber = int(math.floor((random.random() * list_range) + lower_bound))
	random_list.append(newNumber)
	
# write the list to the file
if filename != "":
	outfile = open(filename, "w");
	for x in random_list:
		outfile.write(str(x) + "\n")
	outfile.close()

# print out the list
print "List Generated:"
for x in random_list:
	print x