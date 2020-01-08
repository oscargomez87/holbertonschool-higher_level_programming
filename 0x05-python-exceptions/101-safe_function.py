#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        a = fct(*args)
        return a
    except Exception as e:
        print("Exception: {}".format(e.args[0]), file=stderr)
