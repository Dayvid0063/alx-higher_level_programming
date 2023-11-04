#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    ls = []
    if my_list:
        for u in my_list:
            ls.append(False if u % 2 else True)
        return ls
