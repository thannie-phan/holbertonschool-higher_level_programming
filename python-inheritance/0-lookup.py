#!/usr/bin/python3
"""This module defines a func to lookup attributes, methods of obj."""


def lookup(obj):
    """Returns list of available attributes and methods of an obj.

    Args:
        obj (any): The object to inspect.
    Returns:
        list: list of str rep attributes and methods of the obj
    """
    return dir(obj)
