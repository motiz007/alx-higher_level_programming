#!/usr/bin/python3
"""module documentation"""


def append_write(filename="", text=""):
    """writes text to a file
    Args:
        filename (str): the name of the file
        text (str): the text to write into the file
    Return:
          No. of characters written
    """
    with open(filename, mode='a', encoding='utf-8') as fd:
        num = fd.write(text)
    return num
