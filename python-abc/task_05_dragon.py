#!/usr/bin/python3
"""This module defines mixin class."""

class SwimMixin:
    """Provides swimming capability."""
    def swim(self):
        print('The creature swims!')

class FlyMixin:
    """Provides flying capability."""
    def fly(self):
        print('The creature flies!')

class Dragon(SwimMixin, FlyMixin):
    """This defines class dragon.""" 
    def roar(self):
        print('The dragon roars!')