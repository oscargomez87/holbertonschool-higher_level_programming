#!/usr/bin/python3
"""Sends email in POST request"""
import urllib.request
import urllib.parse
from sys import argv


url = argv[1]
values = {'email': argv[2]}
data = urllib.parse.urlencode(values).encode('ascii')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    print("{}".format(response.read().decode('utf-8')))
