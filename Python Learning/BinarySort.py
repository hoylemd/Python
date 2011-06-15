import sys
import getopt

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

# set the file name
filename = 	"data/numbers.txt"

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
	numbers.append(int(x))

# Print out the initial list	
print "numbers:"
print numbers

# merge sort the list
sorted = mergeSort(numbers)

# Merge Sort	
print "sorted:"
print sorted

# write the results to a file
file = open("results.txt", "w")
for x in sorted:
	file.write(str(x) + "\n")