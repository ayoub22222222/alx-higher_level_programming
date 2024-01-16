#!/usr/bin/python3
""" this module contain a base class
that will manage id attribute in all our
future classes in this projets
"""


class Base:
    """ this class contain a private
    class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """this class take one public attribute
        as a parameter
        args:
            parameter1: intgere
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """this bla bla deadline is about to
        finish
        """
        if list_dictionaries is None:
            list_dictionaries = []

        return json.dumps(list_dictionaries)
