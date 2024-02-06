#!/usr/bin/python3

"""class BaseGeometry (based on 6-base_geometry.py)."""


class BaseGeometry:
    """Base class for geometry shapes"""

    def integer_validator(self, name, value):
        """Validates that value is an integer greater than 0"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Instantiation with width and height"""
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.width = width
        self.height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def __str__(self):
        """Returns a string representation of the
        Rectangle"""
        return f"[Rectangle] {self.width}/{self.height}"


class Square(Rectangle):
    """Square class inherits from rectangle class"""

    def __init__(self, size):
        """instantation with size parameter"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.size = size

    def area(self):
        """Returns the area of the rectangle"""
        return self.size * self.size

    def __str__(self):
        """Returns a string representation of the
        Rectangle"""
        return f"[Rectangle] {self.size}/{self.size}"
