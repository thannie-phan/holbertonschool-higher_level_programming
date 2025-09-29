#!/usr/bin/python3
"""Module returns an obj rep by JSON"""


import json


def from_json_string(my_str):
    """This function returns an obj rep by JSON"""
    return json.loads(my_str)
