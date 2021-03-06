#!/usr/bin/python3
"""get request that handles errors"""
import requests
from sys import argv


if __name__ == "__main__":
    res = requests.get(argv[1])
    try:
        res.raise_for_status()
        print(res.text)
    except:
        print("Error code: {}".format(res.status_code))
