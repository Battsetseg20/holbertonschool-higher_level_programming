#!/usr/bin/python3
"""Module contains a function seve_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation
    json.dump(o) serializes obj as a JSON formatted stream to
    fp (a .write()-supporting file-like object)
    """
    with open(filename, 'w') as file_object:
        json.dump(my_obj, file_object)
