#!/usr/bin/python3
""" Module to find a peak in a list """


def find_peak(list_of_integers):
    """Function to find a peak in a list"""
    if not list_of_integers:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
