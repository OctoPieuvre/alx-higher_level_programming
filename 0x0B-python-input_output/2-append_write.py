#!/usr/bin/python3
"""define a funtion that append a text to a file"""


def append_write(filename="", text=""):
    """a function taht append a text to a file"""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
