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
    if len(text) == 0:
        raise TypeError("text must be a string")
    text = text.strip()
    if len(text) == 0:
        raise TypeError("text must be a string")
    char = 0
    while char < len(text):
        print(text[char], end='')
        if text[char] in ['.', '?', ':']:
            print('\n')
            if char + 1 < len(text) and text[char + 1] == ' ':
                char += 1
                while char < len(text) and text[char] == ' ':
                    char += 1
                continue
        char += 1
        