#!/usr/bin/python3
""" Module contains a function that checks the inheritance"""


def inherits_from(obj, a_class):
    """Returns True if the object is inherited from the class
    False, otherwise"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
