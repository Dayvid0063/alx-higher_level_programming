#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ls = list(a_dictionary.keys())
    ls.sort()
    for u in ls:
        print("{}: {}".format(u, a_dictionary.get(u)))
