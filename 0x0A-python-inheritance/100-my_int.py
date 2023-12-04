#!/usr/bin/python3
"""class MyInt that inherits from int"""


class MyInt(int):
    """int operators == and !=."""

    def __eq__(self, value):
        """return != value"""
        return self.real != value

    def __ne__(self, value):
        """return == value"""
        return self.real == value
