#!/usr/bin/python3
"""Unittest for Rectangle class
"""
import unittest, pep8, json, os, sys
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

    def test_area(self):
        """Test area function"""
        fill

    def test_display(self):
        """Test display function"""
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

    def test_width(self):
        """Test width getter"""
        fill

    def test_height(self):
        """Test height getter"""
        fill

    def test_x(self):
        """test x getter"""
        fill

    def test_y(self):
        """Test y getter"""
        fill

    def test_set_width(self):
        """Test width setter"""
        fill

    def test_set_height(self):
        """Test height setter"""
        fill

    def test_set_x(self):
        """Test x setter"""
        fill

    def test_set_y(self):
        """Test y setter"""
        fill

if __name__ == '__main__':
    unittest.main()
