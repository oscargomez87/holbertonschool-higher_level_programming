#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    result = 0
    for element in argv[1:]:
        result = result + int(element)
    print(result)
