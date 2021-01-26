#!/usr/bin/python3
"""Module contains a function load_from_json_file"""
import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file
    json.load(fp) deserializes fp
    (a .read()-supporting file-like object containing a JSON document)
    to a Python object
    """
    with open(filename) as file_object:
        return json.load(file_object)
