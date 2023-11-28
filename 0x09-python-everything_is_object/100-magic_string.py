#!/usr/bin/python3
"""class LockedClass with no class or object attribute"""


def magic_string():
    magic_string.count = getattr(magic_string, 'count', 0) + 1
    return ", ".join(["BestSchool" for u in range(magic_string.count)])
