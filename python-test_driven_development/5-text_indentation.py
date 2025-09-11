#!/usr/bin/python3
"""The function prints a text with 2 new lines after: . ? and :"""


def text_indentation(text):
    """
    Indent sentence

    Args:
        text: the text to be indented

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in range(len(text)):
        if text[char] == '.' or text[char] == '?' or text[char] == ':':
            print(text[char], end='')
            print()
            print()
            if char + 1 < len(text) and text[char + 1] == ' ':
                continue
        else:
            print(text[char], end='')
            print()
