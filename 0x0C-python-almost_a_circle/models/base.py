#!/usr/bin/python3
# base.py
"""Defines a base model class."""

import json


class Base:
    """Represent the base model.

    Represents the "base" for all other classes in project 0x0C*.

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string repr of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        fname = cls.__name__ + ".json"
        content = []

        if list_objs is not None:
            for items in list_objs:
                items = items.to_dictionary()
                json_dict = json.loads(cls.to_json_string(items))
                content.append(json_dict)

        with open(fname, mode="w") as f:
            json.dump(content, f)
