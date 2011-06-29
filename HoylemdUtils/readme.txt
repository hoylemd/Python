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
	Windows:
		$install.bat
	
	Linux::
		$sudo install.sh
		
	This will install the library to your C:\Python27\Lib\ folder for windows, or /lib/ for linux.  The sudo may or may not be neccesary.  Make sure to add these paths to your PYTHONPATH environment variables.
	If you would rather install the library elsewhere, just copy the hutils folder to the preferred location and make sure PYTHONPATH still points to that location.
	
Testing Instructions:
	run test.py. add the -v flag for additional information