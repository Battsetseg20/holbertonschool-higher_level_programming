#!/usr/bin/python3
"""Contains a class Base"""
import json
import os


class Base():
    """Initializing tha attributes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON str representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file_object:
            if list_objs is None:
                file_object.write('[]')
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                file_object.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    #task19

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Json serialization"""
        filename = cls.__name__ + ".csv"
        if list_objs is None:
            return []
        new_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w') as csv_file:
            csv_file.write(cls.to_json_string(new_list))

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instance"""
        pass
