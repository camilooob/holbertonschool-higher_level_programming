#!/usr/bin/python3
def uniq_add(my_list=[]):
    n_list = set(my_list)
    result = 0
    for a in n_list:
        result += a
    return result
