#!/usr/bin/python3
"""
module: is_same_class
this function check if a given object is
exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """ return true is is an instance of
    a class otherwise it return Flase
    and take two parameter as an argument
    args:
        parameter1: object
        parameter2: class 
    return:
        true or false
    """
    if type(obj) == a_class:
        return True
    else:
        return False
