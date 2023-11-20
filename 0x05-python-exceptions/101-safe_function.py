#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        val = fct(*args)
    except Exception as u:
        print("Exception: {}".format(u), file=sys.stderr)
        return None
    else:
        return val
