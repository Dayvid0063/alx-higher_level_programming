#!/usr/bin/python3
"""Py class-to-JSON function"""


def class_to_json(obj):
    """function that returns the dictionary description"""
    return obj.__dict__
