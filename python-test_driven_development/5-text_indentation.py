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

    segments = []
    current = ""
    pos = 0

    while pos < len(text):
        current += text[pos]
        if text[pos] in ".?:":
            segments.append(current.strip())
            current = ""
        pos += 1

    segments.append(current.strip())
    print("\n\n".join(segments), end="")
