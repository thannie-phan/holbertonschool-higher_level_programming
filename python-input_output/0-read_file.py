#!/usr/bin/python3
"""This is a module to read file"""


def read_file(filename=""):
    """This is a function to read content of file"""
    with open(filename) as file:
        content = file.read()
        print(content, end='')
