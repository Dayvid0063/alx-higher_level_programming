#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """ executes a function safely."""
    try:
        val = fct(*args)
        return val
    except Exception as u:
        print("Exception: {}".format(u), file=sys.stderr)
        return None
