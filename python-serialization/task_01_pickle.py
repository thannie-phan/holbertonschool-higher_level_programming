#!/usr/bin/python3
"""This module serialise and deserialise content using pickle."""


import pickle

class CustomObject:
    """This define class CustomObject"""

    def __init__(self, name, age, is_student):
        """Defines attributes"""
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def display(self):
        """Print out attributes"""
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Is Student: {self.is_student}')
              

    def serialize(self, filename):
        """Serializes and save data to the specified file"""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod

    def deserialize(cls, filename):
        """Deserialise and return an instance of class"""  
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception:
            return None
