#!/usr/bin/python3
"""MyList that inherits from list"""


class MyList(list):
    """list subclass"""
    def __init__(self):
        """initialization"""
        super().__init__()

    def print_sorted(self):
        """sorted list printed"""
        print(sorted(self))
