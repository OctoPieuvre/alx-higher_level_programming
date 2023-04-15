#!/usr/bin/python3
"""Define a function printing a text with 2 new line"""


def text_indentation(text):
    """
    Prints the input text with two new lines after each sentence-ending punctuation mark.

    Args:
        text (str): The input text to format.

    Raises:
        TypeError: If the input is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    sentences = []
    sentence = ""

    for char in text:
        sentence += char
        if char in ".?:":
            sentences.append(sentence.strip())
            sentence = ""

    if sentence:
        sentences.append(sentence.strip())

    for sentence in sentences:
        print(sentence)
        print()
