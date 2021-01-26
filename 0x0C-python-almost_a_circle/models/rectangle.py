#!/usr/bin/python3
"""A subclass Rectangle derived from the Base class"""
from models.base import Base


class Rectangle(Base):
    """Class that models a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the attributes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the x coordinate of the Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """Prints Rectangle instance with charachter #"""
        for i in range(self.__y):
            print("")
        for i in range(self.__height):
            print(' ' * self.__x, end="")
            print('#' * self.__width)

    def __str__(self):
        """Returns str() representation of a Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """*args assigns argument to each attribute
        **kwargs assigns a key/value argument to attributes
        **kwargs can be skipped if args exits and is not empty"""
        if args:
            for n, arg in enumerate(args):
                if n == 0:
                    self.id = arg
                elif n == 1:
                    self.width = arg
                elif n == 2:
                    self.height = arg
                elif n == 3:
                    self.x = arg
                elif n == 4:
                    self.y = arg
        else:
            for name, value in kwargs.items():
                if name is "id":
                    self.id = value
                elif name is "width":
                    self.width = value
                elif name is "height":
                    self.height = value
                elif name is "x":
                    self.x = value
                elif name is "y":
                    self.y = value
