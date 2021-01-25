#!/usr/bin/python3
"""A subclass Square derived from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defining its methods"""

    def __init__(self, size):
        """Initializinging its attributes"""
        super().integer_validator("size", size)
        super().__init__(size, size)  # def area() AttribError:Rectangle__width
        self.__size = size
