# Random integer generation program
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

def generateInts(num_numbers, lower, upper):
	# calculate the range
	list_range = upper - lower

	# seed the random number generator
	random.seed()

	#initialize the list
	new_list = list()

	# generate the random ints
	for i in range(num_numbers):
		newNumber = int(math.floor((random.random() * list_range) + lower))
		new_list.append(newNumber)
		
	return new_list
	
# load default settings
list_length = 25
lower_bound = -100
upper_bound = 100
filename = ""

# parse arguments
arg_count = len(sys.argv)
current_arg = 1
while current_arg < arg_count:
	arg_flag = sys.argv[current_arg]
	arg_value = sys.argv[current_arg+1]
	if arg_flag == "-o":
		filename = arg_value
	elif arg_flag == "-m":
		if isNumeric(arg_value):
			lower_bound = int(arg_value)
		else:
			print "Invalid lower bound \"" + arg_value + "\" specified"
	elif arg_flag == "-M":
		if isNumeric(arg_value):
			upper_bound = int(arg_value)
		else:
			print "Invalid upper bound \"" + arg_value + "\" specified"
	elif arg_flag == "-l":
		if isNumeric(arg_value):
			list_length = int(arg_value)
		else:
			print "Invalid list length \"" + arg_value + "\" specified"
	else:
		print "Invalid argument flag \"" + arg_flag + "\" specified"
	
	current_arg += 2

random_list = generateInts(list_length, lower_bound, upper_bound)
	
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