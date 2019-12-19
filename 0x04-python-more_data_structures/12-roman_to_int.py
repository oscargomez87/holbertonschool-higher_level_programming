#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or roman_string == "None":
        return 0
    romans = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = []
    resum = 0
    for e in roman_string:
        for c in list(romans.keys()):
            if e == c:
                result.append(romans[e])
    print(result)
    for idx, e in enumerate(result):
        print(e)
        if e <= result[idx - 1]:
            resum = resum + e
            print(resum)
        else:
            resum = e - resum
            print(resum)
    return resum
