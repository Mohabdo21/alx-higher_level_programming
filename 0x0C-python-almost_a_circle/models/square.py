#!/usr/bin/python3
"""Module for Square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the Square instance."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''Size of this square.'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the Square instance."""
        return "[{}] ({}) {}/{} - {}".format(
                type(self).__name__, self.id, self.x, self.y, self.width
                )
