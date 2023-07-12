#!/usr/bin/python3
"""module documentation"""


import sys
from os.path import exists

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"
if exists(filename):
    old_args = load_from_json_file(filename)
    old_args.extend(sys.argv[1:])
else:
    old_args = []
save_to_json_file(old_args, filename)
