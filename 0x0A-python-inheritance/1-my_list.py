#!/usr/bin/python3

"""A class that inherits from a superclass"""


class MyList(list):
    """public instamce method that prints the sorted list"""
    def print_sorted(self):
        print(sorted(self))
