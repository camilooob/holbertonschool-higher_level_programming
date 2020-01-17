#!/usr/bin/python3
import math


class MagicClass:
    """Magic Class"""

    def __init__(self, radius=0):
        """Create Radius"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate Area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate Circuference"""
        return 2 * math.pi * self.__radius
