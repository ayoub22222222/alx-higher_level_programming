#!/usr/bin/python3
"""
Module contain a class
square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    defines class Square that inherent from
    a class Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Prints [Square] (<id>) <x>/<y> - <size>"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y,
            self.size)

    @property
    def size(self):
        """return the width"""
        return self.width

    @size.setter
    def size(self, value):
        """Set a new value"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        update the Rectangle value
        """
        if args:
            for k, v in enumerate(args):
                if k == 0:
                    self.id = v
                elif k == 1:
                    self.size = v
                elif k == 2:
                    self.x = v
                else:
                    self.y = v
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """return a dict representation of
        the rectangle information"""
        d = {}
        d["id"] = self.id
        d["size"] = self.size
        d["x"] = self.x
        d["y"] = self.y
        return d
