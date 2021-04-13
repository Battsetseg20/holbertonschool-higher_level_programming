#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the passed URL with
the email as a parameter, and displays the body of the response (decoded
in utf-8)
Manage urllib.error.HTTPError exceptions and print:
Error code: <HTTP status code>
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            the_page = response.read().decode('ascii')
            print(the_page)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
