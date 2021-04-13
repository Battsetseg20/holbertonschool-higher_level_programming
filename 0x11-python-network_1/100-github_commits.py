#!/usr/bin/python3
"""
Please list 10 commits (from the most recent to oldest) of the
repository “rails” by the user “rails”
use Github API
Print all commits by: `<sha>: <author name>` (one by line)
"""

import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])

    commits = requests.get(url).json()
    for i in range(0, 10):
        print("{}: {}".format(
            commits[i].get("sha"),
            commits[i].get("commit").get("author").get("name")))
