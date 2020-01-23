#!/usr/bin/python3
"""
class
My int
"""


class MyInt(int):
    """ Change eq and ne"""
    def __eq__(self, num):
        """ Change == to !="""
        return int(self) != int(num)

    def __ne__(self, num):
        """ Change != to =="""
        return int(self) == int(num)
