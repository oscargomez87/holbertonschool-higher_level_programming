#!/usr/bin/python3
"""Fetches X-Request-Id from header response"""
import requests
from sys import argv


res = requests.get(argv[1])
print(res.headers['X-Request-Id'])
