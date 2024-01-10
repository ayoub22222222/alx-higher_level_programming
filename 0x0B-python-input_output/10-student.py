#!/usr/bin/python3
"""

this module contain a class that return a dictionary
representation of an object
"""


class Student():
    """
    Public Attributes:
        first_name
        last_name
        age
    Public Methods:
        to_json: retrieves its dictionary representation
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes student with full_name las_name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dictionary
        """
	if attrs is None:
		return self.__dict__
	else:
	     dic = {}
	     for i in self.__dict__.key():
		dic[i] = self.__dict__[i]
	     return dic
