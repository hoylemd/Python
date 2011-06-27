# unit tests for hutils

# import the modules
from hutils import general
from hutils import numberLists
import sys

# initialize testing parameters
verbose = False

# parse command-line args
arg = sys.argv.pop()
while arg:
	if arg == "-v":
		verbose = True
	try:
		sys.argv.pop()
	except IndexError:
		arg = None

# initialize global testing fields
numTests = 0
numFailures = 0
testRecord = ["Test Name", "Test Module", "Explanation", "Test ID", "Result", "Feedback", "Raw Result"]
feedbackDatabase = [testRecord]

# test general.readFile
# set up test record
testRecord = ["general.Readfile test", general, "Attempts to apply the function to the \"testdata.txt\" file", 0, False, "None defined", None] 
try:
	testData = general.readFile("testdata.txt")
	testRecord[6]= testData
	if testData != "34\n12\n-64\n87\n-23\n3":
		if verbose:
			print "general.readFile did not return the expected string."
			print "string returned:"
			print testData
			print "\nexpected:"
			print "34\n12\n-64\n87\n-23\n3"
		testRecord[4] = False
		testRecord[5] = "Incorrect string returned."
	else:
		if verbose:
			print "general.readfile functioning as expected."		
		testRecord[4] = True
		testRecord[5] = "Completed successfully"
		
except IOError:
	if verbose:
		print "An error has occurred when trying to open testdata.txt."
		print "Please check that the file exists exists."
	testRecord[4] = False
	testRecord[5] = "IOError when trying to open file."
	testRecord[6] = IOError

# test general.isNumeric
# positive test
# integers
if general.isNumeric("-3"):
	print "general.isNumeric(-3) functioning correctly"
else:
	print "general.isNumeric(-3) failed (False negative.)"
if general.isNumeric("3"):
	print "general.isNumeric(3) functioning correctly"
else:
	print "general.isNumeric(3) failed (False negative.)"
	
# floats
if general.isNumeric("-3.22"):
	print "general.isNumeric(-3.22) functioning correctly"
else:
	print "general.isNumeric(-3.22) failed (False negative.)"
if general.isNumeric("3.22"):
	print "general.isNumeric(3.22) functioning correctly"
else:
	print "general.isNumeric(3.22) failed (False negative.)"

# negative test
if not general.isNumeric("word"):
	print "general.isNumeric(word) functioning correctly"
else:
	print "general.isNumeric(word) failed (False negative.)"

	
# set up the numbers
numList = [34,12,-64,87,-23,3]
sortedList = [-64,-23,3,12,34,87]

# test numberList.mergeSort
testSort = numberLists.mergeSort(numList)

if testSort != sortedList:
	print "numberList.mergeSort failed to sort correctly."
	print "expected:"
	print sortedList
	print "result:"
	print testSort
else:
	print "numberList.mergeSort functioning as expected."