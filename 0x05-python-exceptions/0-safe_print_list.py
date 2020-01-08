#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for idx, y in enumerate(my_list[:x], 1):
            print("{}".format(y), end="")
        print("")
        return idx
    except:
        return idx
