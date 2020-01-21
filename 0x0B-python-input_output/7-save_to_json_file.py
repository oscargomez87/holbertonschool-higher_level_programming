#!/usr/bin/python3
"""Module for task 7"""
import json


def save_to_json_file(my_obj, filename):
    """Writes a JSON representation of an object into a file"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
