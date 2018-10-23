#!/usr/bin/python3
"""Unittest for Base class
"""
import unittest
from models.base import Base

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

    def test_dim_valid(self):
        """Test dimension validator"""
        fill

    def test_coord_valid(self):
        """Test coord validator"""
        fill

    def test_to_json_string(self):
        """Test to_json_string function"""
        fill

    def test_save_to_file(self):
        """Test save_to_file function"""
        fill

    def test_from_json_string(self):
        """Test from_json_string funciton"""
        fill

    def test_create(self):
        """Test create function"""
        fill

    def test_load_from_file(self):
        """Test load_from_file function"""
        fill

if __name__ == '__main__':
    unittest.main()
