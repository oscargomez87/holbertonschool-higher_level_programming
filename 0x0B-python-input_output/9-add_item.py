#!/usr/bin/python3
"""Module for task 9"""
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


try:
    l1 = list(load_from_json_file("add_item.json"))
except Exception as e:
    l1 = []
    save_to_json_file(l1, "add_item.json")
for idx in range(1, len(argv)):
    l1.append(argv[idx])
save_to_json_file(l1, "add_item.json")
