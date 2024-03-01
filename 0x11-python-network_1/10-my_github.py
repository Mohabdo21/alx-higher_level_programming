#!/usr/bin/python3
"""
Puthon script takes GitHub credentials (username, access token), and use
the GitHub API to display user id
"""


import sys

import requests

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    response = requests.get(
            "https://api.github.com/user",
            auth=(username, token)
            )

    try:
        print(response.json().get("id"))
    except ValueError:
        print("Not a valid JSON")
