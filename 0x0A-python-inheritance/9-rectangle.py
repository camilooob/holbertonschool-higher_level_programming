#!/usr/bin/python3

""" Class that inherits from BaseGeometry """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class that inherits from BaseGeometry """

    def __init__(self, width, height):
        """ Constructor """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """ Calculator area """
        return self.__width * self.__height

    def __str__(self):
        """ Print info """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
