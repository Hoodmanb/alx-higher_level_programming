#!/usr/bin/python3

"""class Rectangle that inherits from BaseGeometry (7-base_geometry.py)."""


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


class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Instantiation with width and height"""
        super().__init__()
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
