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
    char = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    delim_found = False
    while char < len(text):
        if text[char] == '.' or text[char] == '?' or text[char] == ':':
            print(text[char])
            delim_found = True
            char += 1
            while char < len(text) and text[char] == ' ':
                char += 1
        else:
            print(text[char], end='')
            char += 1
    if delim_found:
        print()
