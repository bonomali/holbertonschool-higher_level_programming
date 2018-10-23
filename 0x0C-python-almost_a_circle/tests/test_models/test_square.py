#!/usr/bin/python3
"""Unittest for Square class
"""
import unittest, pep8, json, os, sys
from io import StringIO
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base

class TestSquareClass(unittest.TestCase):
    """Test for square class"""

    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0
        cls.r1 = Square(2)
        cls.r3 = Square(5, 1, 1)

    def test_style(self):
        """Tests PEP8 style"""
        fill

    def test_docs(self):
        """Is everything documented?"""
        fill

    def test_basic(self):
        """Test basic functionality of class"""
        fill

    def test_init(self):
        """Test if it initializes correctly"""
        fill

    def test_str(self):
        """Test __str__ overwrite"""
        fill

    def test_update(self):
        """Test update function"""
        fill

    def test_to_dictionary(self):
        """Test to_dictionary funciton"""
        fill

    def test_size(self):
        """Test size getter"""
        fill

    def test_size(self):
        """Test size setter"""
        fill

if __name__ == '__main__':
    unittest.main()
