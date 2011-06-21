Random Ints Readme

Syntax: Ransom Ints.py [-o <outputfile>] [-m <lower_bound>] [-M <upper_bound>] [-l <list_length>]

argument explanation:
	-o specifies a file to write the generated list to
	-m specifies the least allowed value to be generated
	-M specifies the greatest allowed value to be generated
	-l specifies the number of ints to generate
	
If any of these are left undefined, the defaults will be used.
	-o no file.  Output not written.
	-m -100
	-M 100
	-l 25
	
Error Codes:
0 - No error, exited cleanly
1 - Nonnumeric lower bound specified.
2 - Nonnumeric upper bound specified.
3 - Nonnumeric list length specified.
4 - Invalid argument flag supplied. Argument flags are case-sensitive
5 - Argument supplied without flag or flag supplied without argument.
6 - Lower bound is greater than upper bound.