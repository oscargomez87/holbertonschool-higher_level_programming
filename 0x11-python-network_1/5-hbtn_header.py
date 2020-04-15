#!/usr/bin/python3
"""Fetches X-Request-Id from header response"""
import requests
from sys import argv


if __name__ == "__main__":
    res = requests.get(argv[1])
    print(res.headers['X-Request-Id'])
