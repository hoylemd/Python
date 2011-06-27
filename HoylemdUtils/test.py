# unit tests for hutils

# import the modules
from hutils import general
from hutils import numberLists
import sys

# initialize testing parameters
verbose = False

# parse command-line args
for arg in sys.argv:
	if arg == "-v":
		verbose = True

# initialize global testing database
testRecord = ["Test Name", "Test Module", "Explanation", "Test ID", "Result", "Feedback", "Raw Result"]
testDatabase = [testRecord]

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
testDatabase.append(testRecord)

# test general.isNumeric
# negative integers (positive expected)
# set up test record
testRecord = ["general.isNumeric(negative integer) test", general, "Asserts that a negative integer input to the isNumeric function returns positive", 1, False, "None defined", None] 
# conduct test
testRecord[6] = general.isNumeric("-3")
if testRecord[6]:
	if verbose:
		print "general.isNumeric(-3) functioning correctly"
	testRecord[4] = True
	testRecord[5] = "Working as intended."
else:
	if verbose:
		print "general.isNumeric(-3) failed (False negative.)"
	testRecord[4] = False
	testRecord[5] = "False negative on input of <-3>"
testDatabase.append(testRecord)
	
# positive integers (positive expected)
# set up test record
testRecord = ["general.isNumeric(positive integer) test", general, "Asserts that a positive integer input to the isNumeric function returns positive", 2, False, "None defined", None] 
# conduct test
testRecord[6] = general.isNumeric("3")
if testRecord[6]:
	if verbose:
		print "general.isNumeric(3) functioning correctly"
	testRecord[4] = True
	testRecord[5] = "Working as intended."
else:
	if verbose:
		print "general.isNumeric(3) failed (False negative.)"
	testRecord[4] = False
	testRecord[5] = "False negative on input of <3>"
testDatabase.append(testRecord)

# negative floats (positive expected)
# set up test record
testRecord = ["general.isNumeric(negative float) test", general, "Asserts that a negative float input to the isNumeric function returns positive", 3, False, "None defined", None] 
# conduct test
testRecord[6] = general.isNumeric("-3.22")
if testRecord[6]:
	if verbose:
		print "general.isNumeric(-3.22) functioning correctly"
	testRecord[4] = True
	testRecord[5] = "Working as intended."
else:
	if verbose:
		print "general.isNumeric(-3.22) failed (False negative.)"
	testRecord[4] = False
	testRecord[5] = "False negative on input of <-3.22>"
testDatabase.append(testRecord)	
	
# positive floats (positive expected)
# set up test record
testRecord = ["general.isNumeric(positive float) test", general, "Asserts that a positive float input to the isNumeric function returns positive", 4, False, "None defined", None] 
# conduct test
testRecord[6] = general.isNumeric("3.22")
if testRecord[6]:
	if verbose:
		print "general.isNumeric(3.22) functioning correctly"
	testRecord[4] = True
	testRecord[5] = "Working as intended."
else:
	if verbose:
		print "general.isNumeric(3.22) failed (False negative.)"
	testRecord[4] = False
	testRecord[5] = "False negative on input of <3.22>"
testDatabase.append(testRecord)	

# string (negative expected)
# set up test record
testRecord = ["general.isNumeric(string) test", general, "Asserts that a string input to the isNumeric function returns negative", 5, False, "None defined", None] 
# conduct test
testRecord[6] = general.isNumeric("word")
if not testRecord[6]:
	if verbose:
		print "general.isNumeric(word) functioning correctly"
	testRecord[4] = True
	testRecord[5] = "Working as intended."
else:
	if verbose:
		print "general.isNumeric(word) failed (False positive.)"
	testRecord[4] = False
	testrecord[5] = "False positive on input of \"word\""
testDatabase.append(testRecord)	

# list
# boolean
# module
	
# generateInts tests
# test general type functionality
# set up test record
testRecord = ["numberLists.generateInts return type test", numberLists, "Asserts that numberLists returns a list", 6, False, "None defined", None] 
# conduct test
testRecord[6] = numberLists.generateInts(5,0,10)
if type(testRecord[6]) == type(list()):
	if verbose:
		print "numberLists.generateInts(5,0,10) return type functioning correctly."
	testRecord[4] = True
	testRecord[5] = "Working as intended."
else:
	if verbose:
		print "numberLists.generateInts did not return a list"
	testRecord[4] = False
	testRecord[5] = "Did not return a list object."
testDatabase.append(testRecord)
		
# following tests are predicated on previous test's success
if (testRecord[4]):
	# test upper boundaries
	# set up test record
	testRecord = ["numberLists.generateInts upper boundarytest", numberLists, "Asserts that numberLists' upper boundary parameter is applied correctly", 7, False, "None defined", None]
	# conduct test
	testRecord[6] = numberLists.generateInts(10,0,3)
	testRecord[4] = True
	testRecord[5] = "Working as intended."
	for x in testRecord[6]:
		if x > 3:
			if verbose:
				print "numberLists.generateInts generated a number greater than the specified upper bound."
			testRecord[4] = False
			testRecord[5] = "Returned a number greater than the upper boundary."
			break
	testDatabase.append(testRecord)
			
	# test lower boundaries
	# set up test record
	testRecord = ["numberLists.generateInts upper boundarytest", numberLists, "Asserts that numberLists' upper boundary parameter is applied correctly", 8, False, "None defined", None]
	# conduct test
	testRecord[6] = numberLists.generateInts(10,0,3)
	testRecord[4] = True
	testRecord[5] = "Working as intended."
	for x in testRecord[6]:
		if x < 0:
			if verbose:
				print "numberLists.generateInts generated a number less than the specified lower bound."
			testRecord[4] = False
			testRecord[5] = "Returned a number less than the lower boundary."
			break
	testDatabase.append(testRecord)
			
	# test invalid boundaries
	# test list length
	# test 0 list length
	# test negative list length

# calculate stats
numTests = len(testDatabase)
numFailed = 0
numSucceeded = 0

# count success/failures
for record in testDatabase:
	if record[4]:
		numSucceeded += 1
	else:
		numFailed += 1

percentSuccess = (float(numSucceeded) / float(numTests)) * 100	
	
# Report results
print "Total statistics:"
print " " + str(numTests) + " conducted."
print " " + str(numSucceeded) + " succeeded."
print " " + str(numFailed) + " failed."
print " " + str(percentSuccess) + "% of tests succeeded.\n"

print "Failed tests:"
for record in testDatabase:
	if not record[4]:
		print " " + record[0]
		print "  :" + record[5]
