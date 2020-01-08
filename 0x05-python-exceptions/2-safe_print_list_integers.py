#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        num = 0
        for i in my_list:
            if i != (num+1):
                i = num + 1
                x -= 1
            if num < x:
                print("{:d}".format(i), end='')
                num += 1
        print('')
        return num
    except ValueError:
        pass
