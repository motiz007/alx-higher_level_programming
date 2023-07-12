#!/usr/bin/python3
"""module documantation"""


import json


def load_from_json_file(filename):
    """creates an object from JSON object
    Args:
        filename (str): the JSON file
    Return:
          the created object
    """
    with open(filename, encoding='utf-8') as fd:
        my_obj = json.load(fd)
    return my_obj
