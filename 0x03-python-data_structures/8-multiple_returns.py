#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_str = (len(sentence),
                 (sentence[0:1] if len(sentence) != 0 else "None"))
    return tuple_str
