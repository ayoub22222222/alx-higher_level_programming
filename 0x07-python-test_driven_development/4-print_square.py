#!/usr/bin/python3
"""
Module print square
Contains a function  that prints square with #'s
"""


def print_square(size):
    """
    this function take one argument as parameter
    args:
        parameter1: int should be an integer bigger than or 
        equal to zero
    return:
        a square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print("", end="")
    else:
        print("\n".join(["#" * size for rows in range(size)]))
