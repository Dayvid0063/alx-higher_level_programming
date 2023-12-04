#!/usr/bin/python3
"""
MyList class
"""


class MyList(list):
    """contains list"""
    def __init__(self):
        """initialize obj."""
        super().__init__()

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
