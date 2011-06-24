# testUtils.py

# Import the modules to test
from hutils import RandomInts
from hutils import BinarySort
from hutils import BinarySearch

# generate some numbers
my_list = RandomInts.generateInts(10, 0, 25)

# prove it worked
print "RandomInts.generateInts(10,0,25) = "
print my_list

# sort the list
sorted_list = BinarySort.mergeSort(my_list)

print "binarySort.mergeSort(my_list) = "
print sorted_list

# search for the 7th entry from my_list in sorted_list
index = BinarySearch.BSearch(sorted_list, my_list[7])

print str(my_list[7]) + " found at index " + str(index)

