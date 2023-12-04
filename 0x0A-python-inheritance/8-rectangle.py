#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
This module contains a class Rectangle that inherits from BaseGeometry.
"""


class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Instantiation with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
