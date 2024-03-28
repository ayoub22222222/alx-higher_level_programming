#!/usr/bin/python3
""" find the peak element"""


def find_peak(list_of_integers):
    """ 
    find function that take 1 argument as
        a parameter
        arg: list_of_integer paramters one is
        a list of integer
    """
    if len(list_of_integers) == 0:
        return None
    else:
        return max(list_of_integers)
