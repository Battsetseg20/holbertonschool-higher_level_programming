#!/usr/bin/python3
"""Contains a class Base"""


class Base():
    """Initializing tha attributes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects +=1
            self.id = Base.__nb_objects
