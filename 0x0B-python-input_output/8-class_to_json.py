#!/usr/bin/python3
"""module documentation"""


import json


def class_to_json(obj):
    """create a serializable def of the obj"""
    rep = obj.__dict__
    return rep
