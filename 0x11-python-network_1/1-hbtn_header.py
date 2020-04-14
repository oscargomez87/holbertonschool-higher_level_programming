#!/usr/bin/python3
"""prints the header X-Request-Id from a http response"""
import urllib.request
from sys import argv


with urllib.request.urlopen(argv[1]) as response:
    html = response.info()
print(html["X-Request-Id"])
