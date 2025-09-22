#!/usr/bin/python3
"""This module returns True if obj is instance of class, F otherwise"""


def is_same_class(obj, a_class):
    """This module returns True if obj is instance of class, F otherwise """
    if type(obj) is a_class:
        return True
    return False
