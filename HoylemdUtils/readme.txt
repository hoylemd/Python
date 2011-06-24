Hoylemd Utils readme

This is a python package stocked with modules of any utility functions I've written

Package breakdown:

Modules:
	BinarySort	
	BinarySearch
	RandomInts

	
Module breakdown:

BinarySearch:
	Functions:
		isNumeric(number): Returns true if <number> is a number, and false if it is not.
		
		readFile(file_path): Returns the contents of the file describes by <file_path>. Throws IOErrors.
		
		BSearch(num_list, target): Searches <num_list> for <target>. <num_list> must be a sorted list of integers, and target must be an integer. Returns the last occurance of <target> in a sorted list.
		  
BinarySearch:
	Functions:
		isNumeric(number): Returns true if <number> is a number, and false if it is not.
		
		readFile(file_path): Returns the contents of the file describes by <file_path>. Throws IOErrors.
		
		merge(left, right): Accepts two sorted lists of numbers, and merges them such that the resultant list is sorted.
		
		mergeSort(list): Applies the mergeSort algorithm to <list>, a list of numbers and returns a new version of the list, in ascending order.
		
RandomInts:
	Functions:
		isNumeric(number): Returns true if <number> is a number, and false if it is not.
	
		generateInts(num_numbers, lower, upper): returns a list of <num_numbers> integers between <lower> and <upper> inclusive. If <num_numbers> is negative, or <lower> is greater than or equal to <upper>, a blank list will be returned.
		
Installation Instructions:
	Copy the hutils folder to a directory where you keep python modules, and ensure your PYTHONPATH environment variable is set to point to that directory.