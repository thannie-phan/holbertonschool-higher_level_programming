#!/usr/bin/python3
"""This module defines class MyList"""


class MyList(list):
    """This defines class MyList inherits from list. """
    def __init__(self):
        """init comes from list."""
        super().__init__()
    
    def print_sorted(self):
        """Prints the list sort asc."""
        print(sorted(self))
        return sorted(self)
