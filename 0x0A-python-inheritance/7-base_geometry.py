#!/usr/bin/python3
"""Module contains a BaseGeometry class"""


class BaseGeometry:
    """Public instance method: def area(self)"""
    def area(self):
        raise Exception("area() is not implemented")

    """Public instance method: def integer_validator(self, name, value);
    that validates value as an integer"""
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
