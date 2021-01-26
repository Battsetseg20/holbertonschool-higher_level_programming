#!/usr/bin/python3
"""Unittest for module Base"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test for attributes"""

    def test_no_arg(self):
        a = Base()
        b = Base()
        self.assertEqual(a.id, b.id - 1)

    def test_None(self):
        a = Base(None)
        b = Base(None)
        self.assertEqual(a.id, b.id - 1)
