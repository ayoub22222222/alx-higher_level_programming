#!/usr/bin/python3
"""
this module is contain two class one
iherente behvior from the other
"""


class Mylist(list):
    """this class iherente methode
    attribute from class list
    """
    def print_sorted(self):
        """print sorted list"""
        print(sort(self))
