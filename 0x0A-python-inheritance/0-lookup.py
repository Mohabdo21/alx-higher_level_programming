#!/usr/bin/python3
"""
This module contains a function that returns the list of
available attributes and methods of an object.
"""


def lookup(obj):
    """
    Function that returns the list of available attributes
    and methods of an object.

    Args:
        obj: Any object.

    Returns:
        List of the attributes and methods.
    """
    return dir(obj)
