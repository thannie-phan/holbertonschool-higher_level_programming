#!/usr/bin/python3
"""The function adds 2 integers."""


def add_integer(a, b=98):
    """
    Adds two integer

    Args:
        a (int or float): first int
        b (int or float): second int, default is 98

    Returns:
        int: sum of a and b as int
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
