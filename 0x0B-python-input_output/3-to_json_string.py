#!/usr/bin/python3
"""module documantation"""


import json


def to_json_string(my_obj):
    """creates a JSON rep of an object
    Args:
        my_obj (obj): the python object
    Return:
          the created item
    """
    j_str = json.dumps(my_obj)
    return j_str
