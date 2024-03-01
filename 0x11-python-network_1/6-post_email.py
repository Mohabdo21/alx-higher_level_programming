#!/usr/bin/python3
"""
Python script takes a URL and an email, sends a POST request the the passed
URL with the email as a prarameter the displays the response body
"""


import sys

import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {"email": email}
    response = requests.post(url, data=payload)
    print(response.text)
