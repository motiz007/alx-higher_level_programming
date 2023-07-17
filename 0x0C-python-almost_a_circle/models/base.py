#!/usr/bin/python3
"""module documentation"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "{}"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        f_name = cls.__name__ + ".json"
        with open(f_name, mode="w", encoding="utf-8") as fd:
            if list_objs is None:
                fd.write("[]")

            dict_list = []
            for obj in list_objs:
                dict_list.append(obj.to_dictionary())

            fd.write(Base.to_json_string(dict_list))
