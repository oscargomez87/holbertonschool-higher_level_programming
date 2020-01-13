#!/usr/bin/python3
"""prints a modified text"""


def text_indentation(text):
    """Prints a text with double new line on ".", "," or ":"

    Args:
    text (str): text to print
    """
    i = 0
    if type(text) != str:
        raise TypeError("text must be a string")
    while i < len(text):
        print(text[i], end="")
        if text[i] in [".", "?", ":"]:
            print("\n")
            i += 1
        i += 1
