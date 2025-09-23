#!/usr/bin/python3
"""This module defines class Animal."""


from abc import ABC, abstractmethod

class Animal(ABC):
    """This defines class animal from abc module. """
    @abstractmethod
    def sound(self):
        """ abstract method called sound."""
        pass

class Dog(Animal):
    """This defines class Dog that inherits from Animal."""
    def sound(self):
        """This returns sound dog make."""
        return 'Bark'

class Cat(Animal):
    """This defines class Cat that inherits from Animal."""
    def sound(self):
        """This returns sound cat make."""
        return 'Meow'