#!/usr/bin/python3
"""module documentation"""


import sys
from os.path import exists

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"
args_list = []
del sys.argv[0]
for i in sys.argv:
    args_list.append(i)
if exists(filename):
    old_args = load_from_json_file(filename)
    old_args.extend(args_list)
else:
    old_args = args_list
save_to_json_file(old_args, filename)
