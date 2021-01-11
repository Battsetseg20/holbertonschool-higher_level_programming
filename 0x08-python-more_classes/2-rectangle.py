#!/usr/bin/python3
"""Module containing class Rectangle"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """Defines a rectangle by width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get the height attribute"""
        return self.__width

    @height.setter
    def height(self, value):
        """Set the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Returns the rectangle perimeter"""
        return 2 * (self.__height + self.__width)
