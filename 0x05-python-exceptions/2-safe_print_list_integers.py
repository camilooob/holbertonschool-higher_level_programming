#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for i in range(num, x):
        try:
            print("{:d}".format(my_list[i]), end='')
            num += 1
        except (ValueError, TypeError):
            pass
    print()
    return num
