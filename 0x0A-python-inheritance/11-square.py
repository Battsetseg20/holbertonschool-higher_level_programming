#!/usr/bin/python3
"""A subclass Square derived from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defining subclass Square"""

    def __init__(self, size):
        """Initializing its methods and attributes"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Sets the str representation of Square"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
