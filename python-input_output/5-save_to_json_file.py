#!/usr/bin/python3
"""Module writes an obj to a file using JSON"""


import json


def save_to_json_file(my_obj, filename):
    """This function writes an obj to a file using JSON"""
    with open(filename, 'w') as file:
        j_string = json.dumps(my_obj)
        return file.write(j_string)
