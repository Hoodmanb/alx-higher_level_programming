#!/usr/bin/python3

"""a module containing a class that inverts == and !="""


class MyInt(int):

    def __init__(self, value):
        """initializing my class"""
        self.value = value

    def __eq__(self, other):
        """Override the equality operator =="""
        return self.value != other.value

    def __ne__(self, other):
        """Override the inequality operator !="""
        return self.value == other.value
