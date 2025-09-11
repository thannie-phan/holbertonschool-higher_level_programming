#!/usr/bin/python3
"""The function print My name is <first name> <last name>."""


def say_my_name(first_name, last_name=""):
    """
    Print a sentence

    Args:
        first_name: first name
        last_name: last name

    Returns:
        None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
