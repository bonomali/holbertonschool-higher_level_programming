#!/usr/bin/python3
"""Unittest for Square class
"""
import unittest
import pep8
import json
import os
import sys
from io import StringIO
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquareClass(unittest.TestCase):
    """Test for square class"""

    @classmethod
    def setUpClass(cls):
        """Set up class"""
        Square._Square__nb_objects = 0
        cls.s1 = Square(2)
        cls.s2 = Square(5, 1, 1, id=5)

    def test_style(self):
        """Tests PEP8 style"""
        pep = pep8.StyleGuide(quiet=True)
        p = pep.check_files(["models/base.py"])
        self.assertEqual(p.total_errors, 0, "PEP8 errors")

    def test_existence(self):
        """Do all required functions exist?"""
        self.assertTrue(hasattr(Square, "__init__"))
        self.assertTrue(hasattr(Square, "__str__"))
        self.assertTrue(hasattr(Square, "update"))
        self.assertTrue(hasattr(Square, "to_dictionary"))
        self.assertTrue(hasattr(Square, "size"))

    def test_docs(self):
        """Is everything documented?"""
        self.assertTrue(Square.__doc__)
        self.assertTrue(Square.__init__.__doc__)
        self.assertTrue(Square.__str__.__doc__)
        self.assertTrue(Square.update.__doc__)
        self.assertTrue(Square.to_dictionary.__doc__)
        self.assertTrue(Square.size.__doc__)

    def test_basic(self):
        """Test basic functionality of class"""
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 5)

    def test_init(self):
        """Test if it initializes correctly"""
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

    def test_size(self):
        """Test size getter"""
        pass

    def test_size(self):
        """Test size setter"""
        pass
