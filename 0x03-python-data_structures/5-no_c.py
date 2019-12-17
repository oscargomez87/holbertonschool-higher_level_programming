#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for a in my_string:
        if ord(a) != ord('c') and ord(a) != ord('C'):
            new_string = new_string + a
    return new_string
