#!/usr/bin/python3
"""
Python script takes a URL, sends a request and displays the
value of X-Request-Id founded in the header response
"""

import sys

import requests

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
