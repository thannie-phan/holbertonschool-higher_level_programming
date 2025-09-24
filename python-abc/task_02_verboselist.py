#!/usr/bin/python3
"""This module defines class VerboseList."""


class VerboseList(list):
    """This defines class VerboseList from list. """
    def append(self, item):
        """ override append."""
        super().append(item)
        print(f'Added [{item}] to the list.')

    def extend(self, item):
        """ override extend."""
        super().extend(item)
        print(f'Extended the list with [{len(item)}] items.')

    def remove(self, item):
        """ override remove."""
        super().remove(item)
        print(f'Removed [{item}] from the list.')

    def pop(self, index=-1):
        """ override pop."""
        item = self[index]
        print(f'Popped [{item}] from the list.')
        return super().pop(index)
