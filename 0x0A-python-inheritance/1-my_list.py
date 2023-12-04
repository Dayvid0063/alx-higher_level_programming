#!/usr/bin/python3
"""
a class MyList that inherits from list
"""


class MyList(list):
    """contains list"""
    def __init__(self):
        """initialize obj"""
        super().__init__()

    def print_sorted(self):
        """sorted list printed"""
        print(sorted(self))
