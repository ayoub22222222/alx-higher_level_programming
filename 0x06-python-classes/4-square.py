#!/usr/bin/python3
"""make some change on the private attribute"""


class Square:
    """check if the size match with the requerment"""
    def __init__(self, size=0):
        self.__size = size
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """return the size of square"""
        return self.__size ** 2

    @property
    def size(self):
        """return the size value"""
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        elif slef.__size < 0:
            raise ValueError("size must be >= 0")
        else:
            return self.__size

    @__size.Setter
    def size(self, size):
        """update the private attribute"""
        return self.__size = size

