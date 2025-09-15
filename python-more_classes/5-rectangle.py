#!/usr/bin/python3
"""This module defines an empty class Rectangle."""


class Rectangle:
    """This class defines a rectangle by its height and width. """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @width.setter
    def width(self, value):
        """Setter for the width attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter for the height attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width + self.__height) * 2

    def __str__(self):
        """Create a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_line = []
        for row in range(self.__height):
            rectangle_line.append('#' * self.__width)

        return '\n'.join(rectangle_line)

    def __repr__(self):
        """Return a string that can recreate the object with eval()."""
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
