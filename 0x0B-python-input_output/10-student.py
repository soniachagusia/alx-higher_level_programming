#!/usr/bin/python3
"""
Module that defines the class Student
"""


class Student:
    """
    Class to create student instances

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Special method to initialize a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Method that returns a dictionary representation of the Student instance

        Args:
            attrs (list): A list of attribute names to be retrieved.
                If None, all attributes will be retrieved. Default is None.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        obj = self.__dict__.copy()
        if isinstance(attrs, list):
            for item in attrs:
                if not isinstance(item, str):
                    return obj

            d_list = {}
            for iatr in range(len(attrs)):
                for satr in obj:
                    if attrs[iatr] == satr:
                        d_list[satr] = obj[satr]
            return d_list

        return obj

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with
        values from a JSON dictionary.

        Args:
            json (dict): A dictionary containing attribute-value pairs.
        """
        for atr in json:
            self.__dict__[atr] = json[atr]
