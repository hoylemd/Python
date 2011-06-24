# Binary sort program
# Takes in a filename and reads in a list of integers, applies
# Merge Sort to them, and outputs them to stdout.  If a second 
# filename is provided, it will also write the sorted list to 
# that file.

import sys

# numeric validation function
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
	
# merge function
def merge(left, right):
	# calculate the sizes
	lSize, rSize = len(left), len(right)
	
	# initialize the indicies
	lIndex = rIndex = 0
	
	# initialize the list
	list = []
	
	# step through the lists and merge them in order
	while lIndex < lSize and rIndex < rSize:
		if left[lIndex] > right[rIndex]:
			list.append(right[rIndex])
			rIndex += 1
		else:
			list.append(left[lIndex])
			lIndex += 1
	
	# append any leftover bits
	if lIndex < lSize:
		for x in left[lIndex:]:
			list.append(x)
			
	if rIndex < rSize:
		for x in right[rIndex:]:
			list.append(x)
			
	return list

# Merge Sort function
def mergeSort( list ):
	# get the list size
	size = len(list)
	
	# lists of size 1 are already sorted
	if size <= 1:
		return list
		
	# recursively sort the halves
	else:
		middle = size / 2
		left = mergeSort(list[:middle])
		right = mergeSort(list[middle:])
		
		# merge the halves
		merged = merge(left, right)
		return merged