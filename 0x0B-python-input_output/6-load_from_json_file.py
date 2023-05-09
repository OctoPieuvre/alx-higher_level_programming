#!/usr/bin/python3
"""Define a function that creats an object"""
import json


def load_from_json_file(filename):
    """a function that creates an object from JSON File"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
