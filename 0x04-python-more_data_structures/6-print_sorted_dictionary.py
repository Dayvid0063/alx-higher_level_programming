#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    l = list(a_dictionary.keys())
    l.sort()
    for u in l:
        print("{}: {}".format(u, a_dictionary.get[u]))
