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
        """Set up class"""
        Rectangle._Rectangle__nb_objects = 0
        cls.r1 = Rectangle(1, 2)
        cls.r2 = Rectangle(2, 3, 1, 1, id=5)

    def test_style(self):
        """Tests PEP8 style"""
        pep = pep8.StyleGuide(quiet=True)
        p = pep.check_files(["models/base.py"])
        self.assertEqual(p.total_errors, 0, "PEP8 errors")

    def test_existence(self):
        """Do all required functions exist?"""
        self.assertTrue(hasattr(Rectangle, "__init__"))
        self.assertTrue(hasattr(Rectangle, "width"))
        self.assertTrue(hasattr(Rectangle, "height"))
        self.assertTrue(hasattr(Rectangle, "x"))
        self.assertTrue(hasattr(Rectangle, "y"))
        self.assertTrue(hasattr(Rectangle, "area"))
        self.assertTrue(hasattr(Rectangle, "display"))
        self.assertTrue(hasattr(Rectangle, "__str__"))
        self.assertTrue(hasattr(Rectangle, "update"))
        self.assertTrue(hasattr(Rectangle, "to_dictionary"))

    def test_docs(self):
        """Is everything documented?"""
        self.assertTrue(Rectangle.__doc__)
        self.assertTrue(Rectangle.__init__.__doc__)
        self.assertTrue(Rectangle.width.__doc__)
        self.assertTrue(Rectangle.height.__doc__)
        self.assertTrue(Rectangle.x.__doc__)
        self.assertTrue(Rectangle.y.__doc__)
        self.assertTrue(Rectangle.area.__doc__)
        self.assertTrue(Rectangle.display.__doc__)
        self.assertTrue(Rectangle.__str__.__doc__)
        self.assertTrue(Rectangle.update.__doc__)
        self.assertTrue(Rectangle.to_dictionary.__doc__)

    def test_basic(self):
        """Test basic functionality of class"""
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 5)

    def test_area(self):
        """Test area function"""
        self.assertEqual(self.r1.area(), 1 * 2)
        self.assertRaises(TypeError, self.r1.area(), 1)

    def test_display(self):
        """Test display function"""
        pass

    def test_str(self):
        """Test __str__ overwrite"""
        self.assertEqual(self.r1.__str__(), "[Rectangle] (1) 0/0 - 1/2")

    def test_update(self):
        """Test update function"""
        pass

    def test_to_dictionary(self):
        """Test to_dictionary funciton"""
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
