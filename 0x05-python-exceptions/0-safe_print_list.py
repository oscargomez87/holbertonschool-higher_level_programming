#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        for y in range(0, x):
            print("{}".format(my_list[y]), end="")
            counter += 1
        print("")
        return counter
    except:
        print("")
        return counter
