#!/usr/bin/python3
"""make some change on the private attribute"""


class Square:
    """check if the size match with the requerment"""
    def __init__(self, size=0):
        self.size = size

    def area(self):
        """return the size of square"""
        return self.__size ** 2

    @property
    def size(self):
        """return the size value"""
            return self.__size

    @size.Setter
    def size(self, size):
        """update the private attribute"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            return self.__size = size

