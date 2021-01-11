#!/usr/bin/python3
"""Module contains a class representing Rectangle"""


class Rectangle():
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Defines a rectangle by width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__height is 0 or self.__width is 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """Returns the printable representation of the rectangle"""
        if self.__height is 0 or self.__width is 0:
            return ("")
        string = "{}".format('\n'.join(['#' * self.__width
                                        for row in range(0, self.__height)]))
        return (string)

    def __repr__(self):
        """Returns the string representation of rectangle"""
        return ("Rectangle(" + str(self.__width) +
                ", " + str(self.__height) + ")")

    def __del__(self):
        """Print a message for every deletion of a rectangle"""
        print("Bye rectangle...")
