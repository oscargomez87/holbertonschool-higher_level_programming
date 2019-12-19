#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best = max(a_dictionary.values())
    return (list(e for e in a_dictionary.keys() if best == a_dictionary[e])[0])
