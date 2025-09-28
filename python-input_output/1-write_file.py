#!/usr/bin/python3
"""This is a module to write into file"""


def write_file(filename="", text=""):
    """This is a function to write into file"""
    with open(filename, 'w') as file:
        return file.write(text)
