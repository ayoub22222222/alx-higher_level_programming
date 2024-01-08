#!/usr/bin/python3
""" 
this module add_integer
is a funtion that take two argument as a parameter 
both of them are an integer 
"""


def add_integer(a, b=98):
    """ this funtion is take two parametter as 
    an integer and return the sum of two numbers
    
    args:
        param1: (int): the first parameter
        param2: (int): the second parameter
    return:
        retrun the sum of two numbers
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    x = int(a)
    y = int(b)
    results = x + y
    return results
