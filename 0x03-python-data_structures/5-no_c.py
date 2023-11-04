#!/usr/bin/python3
def no_c(my_string):
    text = ""
    for u in my_string:
        if (u != 'c') and (u != 'C'):
            text += u
        return (text)
