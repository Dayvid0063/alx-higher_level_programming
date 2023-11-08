#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    u = list(a_dictionary.keys())
    {a_dictionary.pop(key) for v in u if a_dictionary[v] == value}
    return a_dictionary
