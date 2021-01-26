#!/usr/bin/python3
"""A subclass Rectangle derived from the Base class"""
from models.base import Base


class Rectangle(Base):
    """Class that models a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the attributes"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """Gets the width of the Rectangle"""
            return self.__width

        @width.setter
        def width(self, value):
            """Sets the width value"""
            self.__width = value

        @property
        def height(self):
            """Gets the height of the Rectangle"""
            return self.__height

        @height.setter
        def height(self, value):
            """Sets the height value"""
            self.__height = value

        @property
        def x(self):
            """Gets the x coordinate of the Rectangle"""
            return self.__x

        @x.setter
        def x(self, value):
            """Sets the value of x"""
            self.__x = value

        @property
        def y(self):
            """Gets the y coordinate of the Rectangle."""
            return self.__y

        @y.setter
        def y(self, value):
            """Sets the value of y"""
            self.__y = value
