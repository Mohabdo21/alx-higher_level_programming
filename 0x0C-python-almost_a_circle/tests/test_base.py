#!/usr/bin/python3
"""Module for Base class tests."""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Tests for Base class."""

    def setUp(self):
        """Set up for the tests."""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Test for id."""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_id_edge_cases(self):
        """Test for id edge cases."""
        # Test with negative id
        b6 = Base(-1)
        self.assertEqual(b6.id, -1)

        # Test with zero id
        b7 = Base(0)
        self.assertEqual(b7.id, 0)

        # Test with large id
        b8 = Base(1000000)
        self.assertEqual(b8.id, 1000000)

        # Test with string id
        b9 = Base("100")
        self.assertEqual(b9.id, "100")

        # Test with None id after setting id
        b10 = Base()
        self.assertEqual(b10.id, 1)

    def test_save_to_file(self):
        """Test the save_to_file method."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            content = file.read()
        self.assertEqual(content, '[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]')

        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")


if __name__ == "__main__":
    unittest.main()
