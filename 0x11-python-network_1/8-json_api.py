#!/usr/bin/python3
"""Takes a letter then sends a post request with the letter"""
import requests
from sys import argv


if len(argv) < 2:
    print("No result")
else:
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': argv[1]}
    res = requests.post(url, data)
    try:
        jsonr = res.json()
        if jsonr:
            print("[{}] {}".format(jsonr['id'], jsonr['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
