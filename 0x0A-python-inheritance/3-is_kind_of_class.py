#!/usr/bin/python3

"""a function that checks if an object is an
instance of a class or a class it was inherited from"""


def is_kind_of_class(obj, a_class):
    """returns either true or false"""
    return isinstance(obj, a_class)
