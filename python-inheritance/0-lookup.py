#!/usr/bin/python3
"""This module defines a function to lookup attributes and methods of an object."""
def lookup(obj):
    """Returns the list of available attributes and methods of an object.

    Args:
        obj (any): The object to inspect.
    Returns:
        list: A list of strings representing the attributes and methods of the object.
    """
    return dir(obj)