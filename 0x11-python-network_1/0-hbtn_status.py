#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status using urllib"""
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        thePage = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(thePage)))
        print("\t- content: {}".format(thePage))
        print("\t- utf8 content: {}".format(thePage.decode("utf-8")))
