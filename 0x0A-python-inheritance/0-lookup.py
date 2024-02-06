#!/usr/bin/python3

"""Function that returns the list of available attributes and objects"""


def lookup(obj):
    """return attributes and methods"""
    return dir(obj)
