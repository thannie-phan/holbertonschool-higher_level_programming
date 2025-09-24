#!/usr/bin/python3
"""This module defines class FlyingFish."""

class Fish:
    """This defines class Fish. """

    def swim(self):
        """ abstract method swim."""
        print('The fish is swimming')
    
    def habitat(self):
        """ abstract method habitat."""
        print('The fish lives in water')

class Bird:
    """This defines class Bird. """

    def fly(self):
        """ abstract method swim."""
        print('The bird is flying')
    
    def habitat(self):
        """ abstract method habitat."""
        print('The bird lives in the sky')

class FlyingFish(Bird, Fish):
    """This defines class FlyingFish. """

    def fly(self):
        """ abstract method fly."""
        print('The flying fish is soaring')
    
    def habitat(self):
        """ abstract method habitat."""
        print('The flying fish lives both in water and the sky!')
    
    def swim(self):
        """ abstract method swim."""
        print('The flying fish is swimming')