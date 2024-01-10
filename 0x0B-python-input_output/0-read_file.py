#!/usr/bin/python3
"""
this module contain a function
that read from a file and put it
to the stdout
"""



def read_file(filename=""):
	"""function that take one
	argument as a parameter
	args:
	   parameter1: string 
	"""
	with open(filename, mode="r", encoding="utf-8") as f:
		print(f.read(), end="")
