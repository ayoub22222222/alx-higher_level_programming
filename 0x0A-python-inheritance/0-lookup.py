#!/usr/bin/python3
"""
this function is return the all the atributes inside an object
"""

def lookup(obj):
    """this funtion take one parameter as 
        an argument
        args:
            parameter1: object
        return: 
            all the attribute and methode on that object
    """
    return dir(obj)

