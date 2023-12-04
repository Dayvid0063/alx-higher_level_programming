#!/usr/bin/python3
"""class MyList that inherits from list
"""


class MyList(list):
    """subclass list
    """

    def print_sorted(self):
        """Print self sorted list
        """

        print(sorted(self))
