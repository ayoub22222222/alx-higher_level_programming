#!/usr/bin/python3
"""
Module text identation
Contains a function that prints text with 2 new lines after each ".", "?", and ":"
"""


def text_indentation(text):
    """
    this function take one argument as a parametter
    args:
        parameter1: str
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    list_lines = [lines.strip(' ') for lines in text.split('\n')]
    revised = "\n".join(list_lines)
    print(revised, end="")
