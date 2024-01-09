#!/usr/bin/python3
"""
this module is subclass
that iherent all the methode and atribute
from the BaseGeometry class
"""


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """this class inherent methode from
        the parent class"""
        super().integer_validator("width", width)
        self.width = width
        super().integer_validator("height", height)
        self.height = height
