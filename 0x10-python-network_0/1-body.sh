#!/usr/bin/env bash
#script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -sLX GET "$1"
