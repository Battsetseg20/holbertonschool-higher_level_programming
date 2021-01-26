#!/usr/bin/python3
"""Module contains a function from_json_string"""
import json


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by
    JSON string
    json.loads(s) deserializes a string to a Python object
    """
    return json.loads(my_str)
