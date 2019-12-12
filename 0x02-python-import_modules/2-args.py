#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    print("{:d} arguments.".format(len(argv[1:])) if len(argv[1:]) != 1
          else "{:d} argument:".format(len(argv[1:])))
    for index, element in enumerate(argv[1:], start=1):
        print("{:d}: {}".format(index, element))
