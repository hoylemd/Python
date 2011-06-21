# BinarySearch.py

import sys

# initalize variables
filename = ""
target = 0

# parse arguments
arg_count = len(sys.argv)
current_arg = 1
while current_arg < arg_count:
	
	# handle mismatched arguments
	if current_arg + 1 < arg_count:
		
		# get the argument components
		arg_flag = sys.argv(current_arg)
		arg_value = sys.arg(current_arg+1)
		
		# parse input file
		if arg_flag == "-i":
			filename = arg_value
	else:
		print "Mismatched arguments. Use -<flag> <argument>"
		exit(2)
	
# handle no arguments
if(arg_count == 1):
	print "No arguments specifed."
	exit(1)
	
print "filename: " + filename + "target: " + str(target)