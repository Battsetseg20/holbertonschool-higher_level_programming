#!/usr/bin/python3
"""A subclass Square derived from the Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Super call to use all attributes of Rectangle
        width and height are assigned to the value of size"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overloads the Rectangle class behavior by defined method"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
