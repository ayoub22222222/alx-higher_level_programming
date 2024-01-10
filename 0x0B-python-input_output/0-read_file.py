#!/usr/bin/python3
"""
this module contain a function
that read from a file and put it
to the stdout
"""



def read_file(filename=""):
    """Read and print text from file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
