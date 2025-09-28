#!/usr/bin/python3
"""This is a module to read file"""
def read_file(filename=""):
    """This is a function to read content of file"""
    file = open(filename, "r")
    content = file.read()
    print(content)
    file.close()
