#!/usr/bin/python3
"""This module defines class student."""


class Student:
    """This defines class student. """

    def __init__(self, first_name, last_name, age):
        """This defines attributes of a student obj."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        result = {}
        if attrs is None:
            return self.__dict__

        for key in attrs:
            if key in self.__dict__:
                result[key] = self.__dict__[key]
        return result
    
    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
