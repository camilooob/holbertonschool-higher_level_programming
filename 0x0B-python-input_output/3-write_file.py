#!/usr/bin/python3
def write_file(filename="", text=""):
    """ function that writes a string to a text file (UTF8) and returns the numbe """

    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
