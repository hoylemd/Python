# unit tests for hutils

# import the modules
from hutils import general
from hutils import numberLists

# test general.readFile
try:
	testData = general.readFile("testdata.txt")

	if testData != "34\n12\n-64\n87\n-23\n3":
		print "general.readFile did not return the expected string."
		print "string returned:"
		print testData
		print "\nexpected:"
		print "34\n12\n-64\n87\n-23\n3"
	else:
		print "general.readfile functioning properly"
except IOError:
	print "An error has occurred when trying to open testdata.txt. Check that it exists."

# set up the numbers
numList = [34,12,-64,87,-23,3]
