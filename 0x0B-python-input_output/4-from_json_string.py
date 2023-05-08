#!/usr/bin/python3
"""Define a function tht return an object"""
import json


def from_json_string(my_str):
    """a function that return an object represented by a JSON string"""
    return json.loads(my_str)
