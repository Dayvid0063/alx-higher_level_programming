#!/usr/bin/python3
"""func creates an Object"""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file"""
    with open(filename) as u:
        return json.load(u)
