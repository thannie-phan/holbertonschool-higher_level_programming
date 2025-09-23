#!/usr/bin/python3
"""This module defines class Shape."""


from abc import ABC, abstractmethod


class Shape(ABC):
    """This defines class shape from abc module. """
    @abstractmethod
    def area(self):
        """ abstract method called sound."""
        pass

    def perimeter(self):
        """ abstract method called perimeter."""
        pass


class Circle(Shape):
    """This defines class Circle that inherits from Shape."""
    def __init__(self, radius):
        """This defines the radius of circle."""
        self.radius = radius

    def area(self):
        """This returns area of circle"""
        return 3.141592653589793 * (abs(self.radius) ** 2)

    def perimeter(self):
        """This returns perimeter of circle"""
        return 2 * 3.141592653589793 * abs(self.radius)


class Rectangle(Shape):
    """This defines class Rectangle that inherits from Shape."""
    def __init__(self, width, height):
        """This defines the width and height of rectangle."""
        self.width = width
        self.height = height

    def area(self):
        """This returns area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """This returns perimeter of rectangle"""
        return (self.width + self.height) * 2


def shape_info(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
