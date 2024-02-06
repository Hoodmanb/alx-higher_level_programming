#!/usr/bin/python3

"""class BaseGeometry (based on 6-base_geometry.py)."""


class BaseGeometry:
    """Public instance method: def area(self):
    that raises an Exception with the message area()
    is not implemented"""
    def area(self):
        """return exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks for type and value error"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
