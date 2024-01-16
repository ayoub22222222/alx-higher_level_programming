#!/usr/bin/python3
"""this module contain a class
Rectangle that inherente from
the Base class
"""
from models.base import Base



class Rectangle(Base):
    """this class iherent from the Base class"""
    def __init__(self, height, width, x=0, y=0, id=None):
        """this class take four parameter as an argument
        args:
            parameter1: integer value
            parameter2: int value
            parameter3: int value
            parameter4: int value
            parameter5: None value
        """
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def get_value_height(self):
        """return the height value"""
        return self.__height

    @height.setter
    def get_value_height(self, value):
        """update the height value"""
        if type(value) != int:
            raise TypeError("value must be integer")
        if value < 0:
            raise TypeError("value must be > 0")
        self.__height = value

    @property
    def get_value_width(self):
        """return the current value of width"""
        return self.__width

    @width.setter
    def get_value_width(self, value):
        """update the width value"""
        if type(value) != int:
            raise TypeError("value must be integer")
        if value < 0:
            raise TypeError("value must be > 0")
        self.__width = value

    @property
    def get_value_x(self):
        """return the current value"""
        return self.__x

    @x.setter
    def get_value_x(self, value):
        """update the x vaue"""
        if type(value) != int:
            raise TypeError("value must be integer")
        if value < 0:
            raise TypeError("value must be > 0")
        self.__x = value

    @property
    def get_value_y(self):
        """return the current value of y"""
        return self.__y

    @y.setter
    def get_value_y(self, value):
        """update the y value"""
        if type(value) != int:
            raise TypeError("vaue must be integer")
        if value < 0:
            raise TypeError("vaue must be > 0")
        self.__y = value
