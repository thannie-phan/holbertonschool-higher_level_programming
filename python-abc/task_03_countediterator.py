#!/usr/bin/python3
"""This module defines class CountedIterator."""


class CountedIterator:
    """This defines class CountedIterator """
    def __init__(self, iterable):
        """ This defines class with count iterator."""
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """ This keeps count at all times."""
        return self.counter
    
    def __next__(self):
        """ This redefine next."""
        try:
            item = next(self.iterator)
            self.counter +=1
            return item
        except StopIteration:
            raise StopIteration('No more items')
        
        

        

