#!/usr/bin/python3
def safe_print_integer(value):
    try:
        int(value)
        print(value)
        return True

    except ValueError:
        return False
