#!/usr/bin/python3
"""func inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """inserts text after each line containing a given str in a file"""
    text = ""
    with open(filename) as v:
        for line in v:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as u:
        u.write(text)
