#!/usr/bin/python3
"""Define a function printing a text with 2 new line"""


def text_indentation(text):
    """
    Prints the input text with two new lines after
    each sentence-ending punctuation mark.

    Args:
        text (str): The input text to format.

    Raises:
        TypeError: If the input is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] in ['.', '?', ':']:
            print(text[i])
            print()
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            if text[i] != ' ':
                print(text[i], end='')
            i += 1
