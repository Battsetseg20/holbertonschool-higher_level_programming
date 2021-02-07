#!/usr/bin/python3
"""Includes a subclass Rectangle derived from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle using attributes from  BaseGeometry."""

    def __init__(self, width, height):
        """Intialize the attributes and validates the value"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
