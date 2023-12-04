#!/usr/bin/python3
"""func adds new attribute to an obj. if possible"""


def add_attribute(obj, att, val):
    """add atribute method"""
    if hasattr(obj, '__dict__') is True:
        setattr(obj, att, val)
    else:
        raise TypeError("can't add new attribute")
