#!/usr/bin/python3
"""This module defines a class Square."""


class Square:
    """This class defines a square by its size."""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.__size

    @property
    def position(self):
        """Getter for the position attribute."""
        return self.__position

    @size.setter
    def size(self, value):
        """Setter for the size attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, position):
        """Setter for the position attribute with validation."""
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) for num in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(num >= 0 for num in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the '#' character."""
        if self.__size == 0:
            print("")
            return

        try:
            for empty_row in range(self.__position[1]):
                print()
            for each_row in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
        except Exception as e:
            print(e)
