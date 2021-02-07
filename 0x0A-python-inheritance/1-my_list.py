#!/usr/bin/python3
"""Module contains a class MyList"""


class MyList(list):
    """Subclass MyList derived from the class list"""

    def print_sorted(self):
        """Public instance method print_sorted(self)
        that prints the lists in ascending order"""
        print(sorted(self))
