#!/usr/bin/python3
"""Unittest for Rectangle class
"""
import unittest
import pep8
import json
import os
import sys
from io import StringIO
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestRectangleClass(unittest.TestCase):
    """Test for rectangle class"""

    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0
        cls.r1 = Rectangle(1, 2)
        cls.r3 = Rectangle(2, 3, 1, 1, 5)

    def test_style(self):
        """Tests PEP8 style"""
        pass

    def test_docs(self):
        """Is everything documented?"""
        pass

    def test_basic(self):
        """Test basic functionality of class"""
        pass

    def test_init(self):
        """Test if it initializes correctly"""
        pass

    def test_area(self):
        """Test area function"""
        pass

    def test_display(self):
        """Test display function"""
        pass

    def test_str(self):
        """Test __str__ overwrite"""
        pass

    def test_update(self):
        """Test update function"""
        pass

    def test_to_dictionary(self):
        """Test to_dictionary funciton"""
        pass

    def test_width(self):
        """Test width getter"""
        pass

    def test_height(self):
        """Test height getter"""
        pass

    def test_x(self):
        """test x getter"""
        pass

    def test_y(self):
        """Test y getter"""
        pass

    def test_set_width(self):
        """Test width setter"""
        pass

    def test_set_height(self):
        """Test height setter"""
        pass

    def test_set_x(self):
        """Test x setter"""
        pass

    def test_set_y(self):
        """Test y setter"""
        pass

if __name__ == '__main__':
    unittest.main()
