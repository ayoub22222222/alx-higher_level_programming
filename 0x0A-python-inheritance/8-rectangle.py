#!/usr/bin/python3
"""
this module is subclass
that iherent all the methode and atribute
from the BaseGeometry class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """iherent from the BaseGeometry"""
    def __init__(self, width, height):
        """this class inherent methode from
        the parent class"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
