#!/usr/bin/python3
"""Module creates on obj from JSON"""


import json


def load_from_json_file(filename):
    """This function creates on obj from JSON"""
    with open(filename, 'r') as file:
        object = json.load(file)
        return object
