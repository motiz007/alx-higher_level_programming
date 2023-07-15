#!/usr/bin/python3
"""module documentation"""


class Base:
    """class documentation"""
    __nb_objects = 0
    def __init__(self, id=None):
        """module init
        Args:
            id (int): the item id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
