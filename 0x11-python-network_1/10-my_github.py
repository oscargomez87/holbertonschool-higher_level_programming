#!/usr/bin/python3
"""access a github account, takes user and password"""
import requests
from sys import argv


url = "https://api.github.com/user"
data = {'username': argv[1], 'access_token': argv[2]}
res = requests.get(url, params=data).json()
try:
    print(res['id'])
except KeyError:
    print("None")
