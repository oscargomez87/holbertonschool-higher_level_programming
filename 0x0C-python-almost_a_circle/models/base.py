#!/usr/bin/python3
"""Module for the base class used for
all other classes in this project"""
import json


class Base:
    """Manage id attribute in all future classes and to
    avoid duplicating the same code"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes class attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a JSON representation of a string"""
        if not list_dictionaries:
            return "[]"
        if not isinstance(list_dictionaries, list):
            return "[]"
        if not all(isinstance(item, dict) for item in list_dictionaries):
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves a class representation to a file"""
        clsFile = cls.__name__ + ".json"
        listDict = []
        if list_objs:
            for ins in list_objs:
                listDict.append(ins.to_dictionary())
        with open(clsFile, 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(listDict))

    @staticmethod
    def from_json_string(json_string):
        """returns a list of dictionaries from a JSON string"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        b1 = Base()
        if cls.__name__ == "Rectangle":
            b1 = cls(1, 1)
        else:
            b1 = cls(1)
        b1.update(**dictionary)
        return b1

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        clsFile = cls.__name__ + ".json"
        instanceList = []
        with open(clsFile, 'r', encoding='utf-8') as f:
            for ins in cls.from_json_string(f.read()):
                instanceList.append(cls.create(**ins))
        return instanceList
