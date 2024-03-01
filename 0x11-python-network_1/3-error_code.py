#!/usr/bin/python3
"""
Python script takes a URL, sends a request to it and displays the
body of the response in utf-8
"""


import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        print(f"Error code: {error.code}")
