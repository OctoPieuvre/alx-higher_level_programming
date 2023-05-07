#!/usr/bin/python3
"""Define a function that return a JSON representation"""
import json


def to_json_string(my_obj):
    """a function that return a JSON representation"""
    return json.dumps(my_obj)
