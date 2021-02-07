#!/usr/bin/python3
""" Module contains a function to_json_string"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object(string)
    json.dumps() serializes obj to JSON formattes str"""
    return json.dumps(my_obj)
