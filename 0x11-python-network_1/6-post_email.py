#!/usr/bin/python3
"""Sends post request with an email variable"""
import requests
from sys import argv


if __name__ == "__main__":
    data = {'email': argv[2]}
    res = requests.post(argv[1], data)
    print(res.text)
