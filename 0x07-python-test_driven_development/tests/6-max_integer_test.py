#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_basic(self):
        mylist = [1, 2, 3, 4]
        self.assertEqual(max_integer(mylist), 4)

    def test_outoforder(self):
        mylist = [1, 2, 4, 3]
        self.assertEqual(max_integer(mylist), 4)

    def test_negatives(self):
        mylist = [-1, -2, -3, -4]
        self.assertEqual(max_integer(mylist), -1)

    def test_emptylist(self):
        self.assertEqual(max_integer([]), None)

    def test_one(self):
        self.assertEqual(max_integer([1]), 1)

    def test_strings(self):
        self.assertEqual(max_integer(["one", "two", "three"]), "two")

    def test_mixed(self):
        mylist = [1, 2, "three"]
        self.assertRaises(TypeError, max_integer, mylist)

if __name__ == '__main__':
    unittest.main()
