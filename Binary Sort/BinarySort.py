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

# parse arguments
if len(sys.argv) < 2:
	print "Please specify a file containing the list of numbers."
	print "useage: BinarySort.py <filename> [output file]"
	sys.exit(2)
	
# set the file names
filename = 	sys.argv[1]

if len(sys.argv) > 2:
	outfile = sys.argv[2]
else:
	outfile = ""

# get the data
try:
	file = open(filename, 'r')
except IOError:
	print "No such file \"" + filename + "\""
	sys.exit(1)
data = file.read()
file.close()

# Make the list
list = data.split("\n")
numbers = []
for x in list:
	if isNumeric(x):
		numbers.append(int(x))
	else:
		if x != "\n":
			print "Non-numeric entry in input file \"" + x + "\""
			exit(3)

# Print out the initial list	
print "provided list:"
print numbers
print "\n"

# merge sort the list
sorted = mergeSort(numbers)

# Merge Sort	
print "sorted list:"
print sorted

# write the results to a file
if outfile != "":
	file = open(outfile, "w")
	for x in sorted:
		file.write(str(x) + "\n")
	file.close()