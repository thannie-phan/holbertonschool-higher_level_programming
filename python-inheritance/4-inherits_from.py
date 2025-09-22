#!/usr/bin/python3
"""This module returns True if obj is instance of class that
inherited the specified class. False otherwise"""


def inherits_from(obj, a_class):
    """This module returns T if obj is instance of class that
    inherited specified class. F otherwise """
    if isinstance(obj, a_class) and not type(obj) is a_class:
        return True
    return False
