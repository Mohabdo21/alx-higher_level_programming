#!/usr/bin/python3
"""
Python script takes a repository name and owner name, sends a GET request
to the GitHub API, and displays the 10 most recent commits.
"""


import sys

import requests

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)

    try:
        commits = response.json()
        for commit in commits[:10]:
            print(
                "{}: {}".format(
                    commit.get("sha"),
                    commit.get("commit").get("author").get("name")
                )
            )
    except ValueError:
        print("Not a valid JSON")
