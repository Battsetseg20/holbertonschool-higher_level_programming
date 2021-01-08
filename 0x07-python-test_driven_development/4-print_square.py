#!/usr/bin/python3
"""Module contains function that prints square"""


def print_square(size):
    """Prints square with the charachter #."""
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        [print("#", end="") for column in range(size)]
        print()
