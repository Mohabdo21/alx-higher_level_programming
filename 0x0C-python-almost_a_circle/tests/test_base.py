#!/usr/bin/python3
"""Module for Base class tests."""

import unittest
from models.base import Base


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


if __name__ == "__main__":
    unittest.main()
