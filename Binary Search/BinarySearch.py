# BinarySearch.py

import sys

def isNumeric(number):
	try:
		float(number)
		return True
	except ValueError:
		return False



# initalize variables
filename = None
target = None

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
				exit(3)
		
		# handle invalid flag
		else:
			print "Invalid argument flag provided."
			exit(4)
	else:
		print "Mismatched arguments. Use -<flag> <argument>"
		exit(2)

	# increment argument pointer
	current_arg += 2
	
# handle no arguments
if(arg_count == 1):
	print "No arguments specifed."
	exit(1)
	
# handle unspecified arguments
if filename == None:
	print "No file specified to search."
	exit(5)
if target == None:
	print "No target specified to search for."
	exit(6)