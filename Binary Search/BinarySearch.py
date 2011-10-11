# BinarySearch.py

import sys

def isNumeric(number):
	try:
		float(number)
		return True
	except ValueError:
		return False

def readFile(file_path):
	try:
		data_file = open(filename, 'r')
	except IOError:
		print "No such file \"" + file_path + "\""
		return None
	data = data_file.read()
	data_file.close()
	return data

# Recursive function to implement Binary Search
# returns the index of the first encountered instance of the given target
# note: this is not neccesarily the first occurence in the list
def BSearch(num_list, target):
	# calculate markers
	length = len(num_list)
	radix = length / 2
	middle = num_list[radix]
	
	# apply search
	if middle == target:
		return radix
	else:
		if length > 1:
			# recusion for radix < target
			if middle < target:
				recursive_result =  BSearch(num_list[radix:], target)
						
				# apply radix offset
				if recursive_result != None:
					return recursive_result + radix
				else:
					return None
			# recursion for radix > target
			else:
				return BSearch(num_list[:radix], target)
		else:
			return None
	
# initalize variables
filename = None
target = None
useageString = "Useage: BinarySearch.py -f <filepath> -t <target number>"

# parse arguments
arg_count = len(sys.argv)
current_arg = 1
while current_arg < arg_count:
	
	# handle mismatched arguments
	if current_arg + 1 < arg_count:
		
		# get the argument components
		arg_flag = sys.argv[current_arg]
		arg_value = sys.argv[current_arg+1]
		
		# parse input file
		if arg_flag == "-f":
			filename = arg_value
			
		# parse target
		elif arg_flag == "-t":
			if (isNumeric(arg_value)):
				target = int(arg_value)
			else:
				print "Non-numeric target specified."
				print useageString
				exit(3)
		
		# handle invalid flag
		else:
			print "Invalid argument flag provided."
			print useageString
			exit(4)
	else:
		print "Mismatched arguments. Use -<flag> <argument>"
		print useageString
		exit(2)

	# increment argument pointer
	current_arg += 2
	
# handle no arguments
if(arg_count == 1):
	print "No arguments specifed."
	print useageString
	exit(1)
	
# handle unspecified arguments
if filename == None:
	print "No file specified to search."
	print useageString
	exit(5)
if target == None:
	print "No target specified to search for."
	print useageString
	exit(6)
	
# load in the file
data = readFile(filename)

# handle file read error
if data == None:
	exit(7)

# Make the list
number_list = data.split("\n")
numbers = []
for x in number_list:
	if isNumeric(x):
		numbers.append(int(x))
	else:
		if x != "\n" and x != "":
			print "Non-numeric entry in input file \"" + x + "\""
			exit(8)
			
# apply search
target_index = BSearch(numbers, target)

# report success/failure
if target_index != None:

	# count backwards the number of hits
	hits = 0
	indexPointer = target_index
	while int(number_list[indexPointer]) == target:
		hits += 1
		indexPointer -= 1
	
	# print out the results
	print str(hits),
	if hits == 1:
		print "instance",
	else:
		print "instances",
	print "of " + str(target) + " starting at index " + str(indexPointer+1)
else:
	print "No instances of " + str(target) + " found."
