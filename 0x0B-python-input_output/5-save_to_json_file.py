#!/usr/bin/python3
"""module documantation"""


import json


def save_to_json_file(my_obj, filename):
    """creates a JSON rep of an object
    Args:
        my_obj (obj): the python object
        filename (str): the filename/path
    Return:
          the created item
    """
    with open(filename, mode='w', encoding='utf-8') as fd:
        json.dump(my_obj, fd)
