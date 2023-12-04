#!/usr/bin/python3
"""
a class MyList that inherits from list
"""


class MyList(list):
    """list subclass"""

    def print_sorted(self):
        """
        print sorted list
        """

        print(sorted(self))
