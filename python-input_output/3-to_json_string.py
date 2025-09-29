#!/usr/bin/python3
"""Module returns JSON rep of an obj"""


import json


def to_json_string(my_obj):
    """This function returns JSON rep of an obj"""
    return json.dumps(my_obj)
