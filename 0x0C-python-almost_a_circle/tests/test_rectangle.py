#!/usr/bin/python3
"""Module for Rectangle class tests."""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle class."""

    def setUp(self):
        """Set up for the tests."""
        Rectangle._Base__nb_objects = 0

    def test_id(self):
        """Test for id."""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 7)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 8)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_attributes(self):
        """Test for attributes."""
        r = Rectangle(10, 2, 3, 4)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_attributes_edge_cases(self):
        """Test for attributes edge cases."""
        # Test with negative width
        with self.assertRaises(ValueError):
            r = Rectangle(-10, 2)

        # Test with zero height
        with self.assertRaises(ValueError):
            r = Rectangle(10, 0)

        # Test with negative x
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2, -3, 4)

        # Test with negative y
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2, 3, -4)


if __name__ == "__main__":
    unittest.main()
