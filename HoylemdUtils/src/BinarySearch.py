# BinarySearch.py

import sys

# function to check if a variable is a number
def isNumeric(number):
	try:
		float(number)
		return True
	except ValueError:
		return False

# function to read in the contents of a file and return the data
def readFile(file_path):
	data_file = open(filename, 'r')
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