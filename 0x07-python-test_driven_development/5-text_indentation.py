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

    punctuations = [".", "?", ":"]
    new_text = ""
    for i in range(len(text)):
        if text[i] in punctuations:
            new_text += text[i] + "\n\n"
            if i < len(text) - 1 and text[i+1] == " ":
                i += 1
        else:
            new_text += text[i]

    print("\n".join(line.strip() for line in new_text.split("\n")))
