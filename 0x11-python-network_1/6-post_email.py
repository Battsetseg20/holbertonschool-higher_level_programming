#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the passed URL with
the email as a parameter, and displays the body of the response.
Using requests package
"""

import requests
from sys import argv

if __name__ == "__main__":
    req = requests.post(argv[1], {'email': argv[2]})
    print(req.text)
