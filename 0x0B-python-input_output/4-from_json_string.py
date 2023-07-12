#!/usr/bin/python3
"""module documantation"""


import json


def from_json_string(my_str):
    """creates an object from JSON str
    Args:
        my_str (str): the python object
    Return:
          the created item
    """
    py_obj = json.loads(my_str)
    return py_obj
