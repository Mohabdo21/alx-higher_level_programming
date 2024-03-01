#!/usr/bin/python3
"""
Python script takes in a URL, sends a request the the URL and displays
the response body
"""


import sys

import requests

if __name__ == "__main__":
    try:
        response = requests.get(sys.argv[1])
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError as error:
        print(f"Error code: {error.response.status_code}")
