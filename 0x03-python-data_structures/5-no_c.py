#!/usr/bin/env python3
def no_c(my_string):
    new_string = my_string.translate({ord('C'): None, ord('c'): None})
    return new_string

