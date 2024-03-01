#!/usr/bin/python3
"""
Python scipt takes a URL, sends a request to the URL and
Displays the value of the key X-Request-Id from the response header
"""


import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get("X-Request-Id"))
