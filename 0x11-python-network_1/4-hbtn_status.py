#!/usr/bin/python3
"""Uses requests package to fetch url"""
import requests


res = requests.get('https://intranet.hbtn.io/status')
print("Body response:\n\t- type: {}\n\t- content: {}"
      .format(type(res.text), res.text))
