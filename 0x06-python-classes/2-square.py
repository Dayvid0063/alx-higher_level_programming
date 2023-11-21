#!/usr/bin/python3
"""class square definition"""


class Square:
    """square representation"""
    def __init__(self, size=0):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size
