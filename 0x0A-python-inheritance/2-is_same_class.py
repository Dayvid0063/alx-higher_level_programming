#!/usr/bin/python3
"""class-checking func."""


def is_same_class(obj, a_class):
    """verifies if an obj. is exactly an instance"""
    if type(obj) == a_class:
        return True
    return False
