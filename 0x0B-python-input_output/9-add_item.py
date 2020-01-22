#!/usr/bin/python3

from sys import argv
from os import path

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"

if path.isfile(filename):
    mylist = load_from_json_file(filename)
else:
    mylist = []

mylist += sys.argv[1:]
save_to_json_file(my_list, filename)
