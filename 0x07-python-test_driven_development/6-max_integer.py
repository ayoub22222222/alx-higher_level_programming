#!/usr/bin/python3
"""
Module tahat contain a function 
that return the maximum value of an integer
"""


def max_integer(list=[]):
    """this function that take one parameter as an argument
       args:
            parameter1: list of a random integer
       return:
        the maximum value of an integer
    """
    if len(list) == 0:
        return None
    max_value = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            max_value = list[i]
        i += 1
    return max_value
