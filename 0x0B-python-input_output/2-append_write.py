#!/usr/bin/python3
"""func appends a string"""


def append_write(filename="", text=""):
    """appends string to the end of a UTF8 text file"""
    with open(filename, "a", encoding="utf-8") as u:
        return u.write(text)
