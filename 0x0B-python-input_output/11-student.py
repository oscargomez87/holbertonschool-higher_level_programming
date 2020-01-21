#!/usr/bin/python3
"""Module that defines a class"""
import json


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialzies attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return json.loads(json.dumps(self.__dict__))
