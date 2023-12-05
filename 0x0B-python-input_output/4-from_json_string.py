#!/usr/bin/python3
"""func returns an object (Python data structure)"""
import json


def from_json_string(my_str):
    """return representation of a JSON string"""
    return json.loads(my_str)
