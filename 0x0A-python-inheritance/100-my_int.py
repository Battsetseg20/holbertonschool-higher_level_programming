#!/usr/bin/python3
"""Class MyInt that inherits from int"""


class MyInt(int):
    """Inverts == and != operators"""

    def __eq__(self, x):
        """Overloads == operator with defined behavior"""
        return int(self) != x

    def __ne__(self, x):
        """Overloads != operator with defined behavior"""
        return int(self) == x
