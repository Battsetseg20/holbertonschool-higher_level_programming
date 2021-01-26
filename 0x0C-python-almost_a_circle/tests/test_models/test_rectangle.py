#!/usr/bin/python3
"""Unittest for Rectangle"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Basic tests"""

    def test_if_subclass(self):
        self.assertTrue(issubclass(Rectangle, Base))
