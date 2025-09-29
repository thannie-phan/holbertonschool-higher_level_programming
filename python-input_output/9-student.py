#!/usr/bin/python3
"""This module defines class student."""


class Student:
    """This defines class student. """
    pass

    def __init__(self, first_name, last_name, age):
        """This defines attributes of a student obj."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
