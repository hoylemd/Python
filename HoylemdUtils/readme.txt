Hoylemd Utils readme

This is a python package stocked with modules of any utility functions I've written

Package breakdown:

Modules:
	numberLists
	general

	
Module breakdown:

numberLists:
	Functions:
		generateInts(num_numbers, lower, upper): returns a list of <num_numbers> integers between <lower> and <upper> inclusive. If <num_numbers> is negative a blank list will be returned. If <upper> is less than <lower>, a list will be generated with the boundaries switched to reflect the probable intention of the call, so the actual order of <lower> and <upper> isn't impoertant as long as they come after <num_numbers>.
		
general:
	Functions:
		isNumeric(number): Returns true if <number> is a number, and false if it is not.
		
		readFile(file_path): Returns the contents of the file describes by <file_path>. Throws IOErrors.
		
Installation Instructions:
	Copy the hutils folder to a directory where you keep python modules, and ensure your PYTHONPATH environment variable is set to point to that directory.
	
Testing Instructions:
	run test.py. add the -v flag for additional information