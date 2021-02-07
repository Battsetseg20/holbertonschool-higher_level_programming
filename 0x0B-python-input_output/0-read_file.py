#!/usr/bin/python3
"""Module contains a function that reads a text file"""


def read_file(filename=""):
    """Reads txt file and prints it to stdout"""
    with open(filename) as file_object:
        contents = file_object.read()
        print(contents, end="")
