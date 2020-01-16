#!/usr/bin/python3
class Rectangle:
    """ Init Class width set 0 and height set 0"""

    def __init__(self, width=0, height=0):
        """ Constructor """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Width Getter """

        return self.__width

    @width.setter
    def width(self, value):
        """ Width Setter """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Height Getter """

        return self.__height

    @height.setter
    def height(self, value):
        """ Height Setter """

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value