#!/usr/bin/python3
""" 
this Module
conataine a function that print the full name of a user
"""


def say_my_name(first_name, last_name=""):
    """
    this function take two parameter as an argument 
    args:
        parater1: str 
        parameter2: str
    return:
        print the full name 
    """
    if isinstance(first_name, str) and isinstance(last_name, str):
        print("My name is {:s} {:s}".format(first_name, last_name))
    else:
        raise TypeError("{:s} must be a string".
                        format("first_name" if isinstance(last_name, str)
                               else "last_name"))
