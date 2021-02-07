#!/usr/bin/python3
"""A subclass Square derived from the Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Super call to use all attributes of Rectangle
        width and height are assigned to the value of size"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value

    def __str__(self):
        """Overloads the Rectangle str behavior by defined method"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """*args assigns argument to each attribute
        **kwargs assigns a key/value argument to attributes
        **kwargs can be skipped if args exits and is not empty"""
        if args:
            for n, arg in enumerate(args):
                if n == 0:
                    self.id = arg
                elif n == 1:
                    self.size = arg
                elif n == 2:
                    self.x = arg
                elif n == 3:
                    self.y = arg
        else:
            for name, value in kwargs.items():
                if name is "id":
                    self.id = value
                elif name is "size":
                    self.width = value
                elif name is "x":
                    self.x = value
                elif name is "y":
                    self.y = value

    def to_dictionary(self):
        """Returns dictionary representation of a Square"""
        return {
            "id": self.id,
            "x": self.x,
            "y": self.y,
            "size": self.width,
            }
