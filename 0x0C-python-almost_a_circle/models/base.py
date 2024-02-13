#!/usr/bin/python3

class Base:
    """
    a class to manage all id attributes in
    other classes to avoid duplicating same code
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        a constructor that takes two parameters
        id and self
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
