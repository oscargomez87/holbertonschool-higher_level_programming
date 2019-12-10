#!/usr/bin/python3
def uppercase(str):
    for c in range(len(str)):
        print("{}".format(chr(ord(str[c]) - 32), end='')
              if (ord(str[c]) >= 97 and ord(str[c]) <= 122)
              else "{}".format(str[c]), end='')
    print()
