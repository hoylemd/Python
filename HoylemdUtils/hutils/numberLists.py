# hutils.numberLists module

import random
import math

# fucntion to search a sorted list for a value
def binarySearch(num_list, target):
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

# function to generate a list of random integers
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