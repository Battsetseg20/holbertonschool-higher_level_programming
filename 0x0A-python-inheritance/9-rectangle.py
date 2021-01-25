#!/usr/bin/python3
"""Includes a subclass Rectangle derived from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle using attributes from  BaseGeometry."""

    def __init__(self, width, height):
        """Intialize the attributes and validates the value"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns str() representation of a Rectangle"""
        w = str(self.__width)
        h = str(self.__height)
        return "[Rectangle] " + w + "/" + h
