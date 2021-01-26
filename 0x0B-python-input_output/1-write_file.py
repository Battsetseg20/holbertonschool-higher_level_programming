#!/usr/bin/python3
"""Contains function write_file"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8)
    Returns the number of characters written
    """
    with open(filename, 'w') as file_object:
        return file_object.write(text)
