#!/usr/bin/python3
"""Define a file that write in a file"""


def write_file(filename="", text=""):
    """a fonction that write a text in a file.

        Args:
            filename (str): the name of the file
            text (str): the thxt to write to file
        Return:
            number of character
    """
    with open(filename, 'w', encoding='utf-8') as file:
        content = file.write(text)
        return content
