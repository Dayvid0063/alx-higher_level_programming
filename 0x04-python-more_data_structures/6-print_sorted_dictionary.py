#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list(a_dictionary.keys())
    list(a_dictionary.keys()).sort()
    for u in list(a_dictionary.keys()):
        print("{}: {}".format(u, a_dictionary.get[u]))
