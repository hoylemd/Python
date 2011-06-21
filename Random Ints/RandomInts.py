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
		newNumber = int(math.floor((random.random() * list_range) 
		 + lower))
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
	
	# validate argument-flag matching
	if (current_arg + 1 < arg_count):
	
		# get the flag and argument
		arg_flag = sys.argv[current_arg]
		arg_value = sys.argv[current_arg+1]
		
		# parse output file
		if arg_flag == "-o":
			filename = arg_value
		
		# parse lower bound
		elif arg_flag == "-m":
			if isNumeric(arg_value):
				lower_bound = int(arg_value)
			else:
				print "Invalid lower bound \"" + arg_value + "\" specified"
				exit(1)
				
		# parse upper bound
		elif arg_flag == "-M":
			if isNumeric(arg_value):
				upper_bound = int(arg_value)
			else:
				print "Invalid upper bound \"" + arg_value + "\" specified"
				exit(2)
				
		#parse list length
		elif arg_flag == "-l":
			if isNumeric(arg_value):
				list_length = int(arg_value)
			else:
				print "Invalid list length \"" + arg_value + "\" specified"
				exit(3)
		
		# handle invalid arguments
		else:
			print "Invalid argument flag \"" + arg_flag + "\" specified"
			exit(4)
		
		current_arg += 2
	
	# handle mismatched arguments/flags
	else:
		print "Mismatched arguments. Use -<flag> <argument>"
		exit(5)

# validate arguments
if lower_bound > upper_bound:
	print "Lower bound is greater than upper bound. Define both explicitly to avoid this error."
	exit(6)

# generate the list
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
	
# exit cleanly
exit(0)