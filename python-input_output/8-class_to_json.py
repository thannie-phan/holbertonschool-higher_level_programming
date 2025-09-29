#!/usr/bin/python3
"""Module takes an obj and return a dict that describe it"""


def class_to_json(obj):
    """This function takes an obj and return a dict that describe it"""
    result = obj.__dict__
    return result
