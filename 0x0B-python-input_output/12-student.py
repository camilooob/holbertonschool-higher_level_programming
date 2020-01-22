#!/usr/bin/python3
class Student:
    """Class Student"""
    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if not isinstance(attrs, list) or \
        not all(isinstance(i, str) for i in attrs):

            dic = self.__dict__.copy()

        else:

            dic = {i: self.__dict__[i] for i in attrs if i in self.__dict__}

        return dic
