#!/usr/bin/python3
"""Define a function that read a file"""


def read_file(filename=""):
    """a function that read a UTF8 file"""
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content, end="")
