#!/usr/bin/python3
"""Module for task 10"""
import json


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object"""
    return json.loads(json.dumps(obj.__dict__))
