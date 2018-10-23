#!/usr/bin/python3
"""Unittest for Base class
"""
import unittest
import pep8
import json
import os
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """Test for base class"""

    @classmethod
    def setUpClass(cls):
        """Instances for testing on"""
        cls.base1 = Base()
        cls.base2 = Base(5)
        cls.base3 = Base()
        cls.base4 = Base()
        cls.rectangle1 = Rectangle(1, 2, 1, 1, id=6)
        cls.rectangle2 = Rectangle(2, 3, id=7)
        cls.square1 = Square(3, id=8)
        cls.square2 = Square(5, 2, 2, id=9)

    @classmethod
    def tearDownClass(cls):
        """Tear down instances that were set up"""
        del cls.base1
        del cls.base2
        del cls.base3
        del cls.base4
        # cls._Base__nb_objects = 0

    def test_style(self):
        """Tests PEP8 style"""
        pep = pep8.StyleGuide(quiet=True)
        p = pep.check_files(["models/base.py"])
        self.assertEqual(p.total_errors, 0, "PEP8 errors")

    def test_existence(self):
        """Do all required functions exist?"""
        self.assertTrue(hasattr(Base, "__init__"))
        self.assertTrue(hasattr(Base, "create"))
        self.assertTrue(hasattr(Base, "to_json_string"))
        self.assertTrue(hasattr(Base, "from_json_string"))
        self.assertTrue(hasattr(Base, "save_to_file"))
        self.assertTrue(hasattr(Base, "load_from_file"))

    def test_docs(self):
        """Is everything documented?"""
        self.assertTrue(Base.__doc__)
        self.assertTrue(Base.__init__.__doc__)
        self.assertTrue(Base.create.__doc__)
        self.assertTrue(Base.to_json_string.__doc__)
        self.assertTrue(Base.from_json_string.__doc__)
        self.assertTrue(Base.save_to_file.__doc__)
        self.assertTrue(Base.load_from_file.__doc__)

    def test_basic(self):
        """Test basic functionality of class"""
        self.assertEqual(self.base1.id, 1)
        self.assertEqual(self.base2.id, 5)
        self.assertEqual(self.base3.id, 2)
        self.assertEqual(self.base4.id, 3)

    def test_dim_valid(self):
        """Test dimension validator"""
        self.assertRaises(TypeError, Base.dimension_validator, -1)
        self.assertRaises(TypeError, Base.dimension_validator, "a")

    def test_coord_valid(self):
        """Test coord validator"""
        self.assertRaises(TypeError, Base.coord_validator, -1)
        self.assertRaises(TypeError, Base.coord_validator, "a")

    def test_to_json_string(self):
        """Test to_json_string function"""
        dict = self.rectangle1.to_dictionary()
        dict2 = {'width': 1, 'height': 2, 'x': 1, 'y': 1, 'id': 6}
        jsonstring = Base.to_json_string([dict])
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(dict, dict2)

    def test_save_to_file(self):
        """Test save_to_file function"""
        result = [{"y": 1, "x": 1, "id": 6, "width": 1, "height": 2},
                  {"y": 0, "x": 0, "id": 7, "width": 2, "height": 3}]
        Rectangle.save_to_file([self.rectangle1, self.rectangle2])
        self.assertTrue(os.path.isfile("Rectangle.json"))
        with open("Rectangle.json", "r") as file:
            self.assertEqual(result, json.load(file))

    def test_from_json_string(self):
        """Test from_json_string function"""
        list = [{'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}]
        test = Rectangle.to_json_string(list)
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string(test), list)

    def test_create(self):
        """Test create function"""
        dict = self.rectangle1.to_dictionary()
        other_rect = Rectangle.create(**dict)
        self.assertFalse(self.rectangle1 is other_rect)
        self.assertFalse(self.rectangle1 == other_rect)

    def test_load_from_file(self):
        """Test load_from_file function"""
        rect1 = self.rectangle1
        rect2 = self.rectangle2
        result = [rect1, rect2]
        Rectangle.save_to_file(result)
        list = Rectangle.load_from_file()
        self.assertNotEqual(result, list)
