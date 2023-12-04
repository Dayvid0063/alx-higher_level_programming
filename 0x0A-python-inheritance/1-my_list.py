#!/usr/bin/python3
"""MyList function
"""


class MyList(list):
    """subclass list
    """

    def print_sorted(self):
        """Prints self sorted list
        """

        print(sorted(self))
