#!/usr/bin/python3
"""Module that defines a class"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialzies attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        dic = {}
        if not isinstance(attrs, list):
            return self.__dict__
        if all(isinstance(le, str) for le in attrs):
            for e in attrs:
                if e in self.__dict__:
                    dic[e] = self.__dict__.get(e)
        else:
            dic = self.__dict__
        return dic
