#!/usr/bin/python3
"""This module returns T if obj is instance of class that inherited
from the specified class. F otherwise"""


def inherits_from(obj, a_class):
    """This module returns T if obj is of class or inherited from
specified class. F otherwise """
    if isinstance(obj, a_class) and not type(obj) is a_class:
        return True
    return False
