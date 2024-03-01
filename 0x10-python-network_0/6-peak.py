#!/usr/bin/python3
"""find_peak to find a peak from a given list"""


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers.

    This function uses a binary search algorithm for efficiency.

    Args:
        list_of_integers (list): The list of integers in which to find a peak.

    Returns:
        int: The value of a peak in the list, if one exists.
        If the list is empty, returns None.
    """
    if not list_of_integers:
        return None

    low_index = 0
    high_index = len(list_of_integers) - 1

    while low_index < high_index:
        mid_index = (low_index + high_index) // 2

        if list_of_integers[mid_index] < list_of_integers[mid_index + 1]:
            low_index = mid_index + 1  # Move the lower index to the right
        else:
            high_index = mid_index  # Move the higher index to the left

    # When low_index == high_index, we've found a peak
    return list_of_integers[low_index]
