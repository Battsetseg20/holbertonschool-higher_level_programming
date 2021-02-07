#!/usr/bin/python3
"""A function that adds attibutes to objects"""


def add_attribute(obj, attribute, value):
    """Add a new attribute to an object if possible.
    Raises TypeError: If the attribute cannot be added."""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
