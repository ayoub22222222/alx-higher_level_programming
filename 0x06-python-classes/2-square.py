#!/usr/bin/python3
"""make some change on the private attribute"""



class Square:
    """check if the size match 
        with the requerment"""
    def __init__(self, size=0):
        self.__size = size
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
