#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    u = my_list[:]
    if 0 <= idx < len(my_list):
        u[idx] = element
        return(u)
    return(my_list)
