#!/usr/bin/python3
""" Rectangle Class """
from models.base import Base


class Rectangle(Base):
    """Constructor """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ Width Getter - Read Value """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter width - change value """
        self.__width = value

    @property
    def height(self):
        """ height Getter - Read Value """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter height - change value """
        self.__height = value

    @property
    def x(self):
        """ x Getter - Read Value """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter x - change value """
        self.__x = value

    @property
    def y(self):
        """ y Getter - Read Value """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter y - change value """
        self.__y = value
