#!/usr/bin/python3
"""This module returns True if obj is instance of class or inherited class. F otherwise"""


def is_kind_of_class(obj, a_class):
    """This module returns True if obj is of class or inherited class. F otherwise """
    if type(obj) is a_class or isinstance(obj, a_class):
        return True
    return False
