#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or roman_string == "None":
        return 0
    if not hasattr(roman_string, "__iter__"):
        return 0
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    resum = 0
    for st in range(len(roman_string)):
        if st > 0 and romans[roman_string[st]] > romans[roman_string[st - 1]]:
            resum += romans[roman_string[st]] - 2 * romans[roman_string[st - 1]]
        else:
            resum += romans[roman_string[st]]
    return resum
