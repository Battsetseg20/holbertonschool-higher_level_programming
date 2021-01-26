#!/usr/bin/python3
"""Unittest for Square module"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class testSquare(unittest.TestCase):
    """Basic tests"""

    def test_if_subclass(self):
        self.assertTrue(issubclass(Square, Rectangle))

