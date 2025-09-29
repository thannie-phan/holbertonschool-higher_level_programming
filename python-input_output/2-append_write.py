#!/usr/bin/python3
"""This is a module to append to end of file"""


def append_write(filename="", text=""):
    """This is a function to append to end of file"""
    with open(filename, 'a') as file:
        return file.write(text)
