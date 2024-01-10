#!/usr/bin/python3
"""
ithis module conatin a function that
returns Json representation of obj
"""
import json


def to_json_string(my_obj):
    """this function take one parameter as an argument
    Args:
	parameter1: my_obj: python object
    Return:
        json string representation
    """
    return json.dumps(my_obj)
