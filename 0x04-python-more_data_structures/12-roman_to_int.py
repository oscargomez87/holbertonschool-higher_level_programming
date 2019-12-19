#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or roman_string == "None":
        return 0
    if not hasattr(roman_string, "__iter__"):
        return 0
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = []
    resum = 0
    for e in roman_string:
        for c in list(romans.keys()):
            if e == c:
                result.append(romans[e])
    if len(result) < 2:
        return result[0]
    for idx, e in enumerate(result):
        if idx < len(result) - 1:
            if e >= result[idx + 1]:
                resum = resum + e
            else:
                if e > resum:
                    resum = e - resum
                else:
                    resum = resum - e
        else:
            resum = resum + e
    return resum
