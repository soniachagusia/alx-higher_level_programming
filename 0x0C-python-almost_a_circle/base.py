#!/usr/bin/python3
"""Unit tests for Base class"""

import unittest
import csv
import json

"""
This module defines the Base class.

The Base class is the "base" of all other classes in the project.
It manages the id attribute and provides a common implementation
for generating unique ids like the ones we are given in the 0-main.py file
"""


class Base:
    """
    The Base class represents the base class for all other
    classes in the project.

    Attributes:
        __nb_objects (int): A private class attribute that keeps track of
        the number of objects created. Used for generating unique ids.
        id (int): A public instance attribute that stores the
        unique id of an object.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int, optional): The id value to assign to the object.
            If provided, the id attribute will be set to this value.
            If not provided, a new unique id will be generated based on
            the __nb_objects attribute.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            cls: The class.
            list_objs (list): List of instances to be serialized.

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                json_str = cls.to_json_string(list_dicts)
                file.write(json_str)
            else:
                file.write("[]")

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of dictionaries represented by json_string.

        Args:
            json_string (str): JSON string.

        Returns:
            list: List of dictionaries represented by json_string.
        """
        return json.loads(json_string) if json_string else []

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with attributes set based on dictionary.

        Args:
            cls: The class.
            **dictionary: Double pointer to a dictionary

        Returns:
            obj: An instance with attributes set based on dictionary.
        """
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            new_instance = cls(1)
        else:
            return None

        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances loaded from a file.

        Args:
            cls: The class.

        Returns:
            list: List of instances loaded from a file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_str = file.read()
                list_dicts = cls.from_json_string(json_str)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV
        Args:
           list_objs(list): List of objects"""
        filename = "{}.csv".format(cls.__name__)
        data = []
        if list_objs is not None:
            for obj in list_objs:
                dictionary = obj.to_dictionary()
                data.append(dictionary)
        rectangle_header = ['id', 'width', 'height', 'x', 'y']
        square_header = ['id', 'size', 'x', 'y']
        with open(filename, mode='w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                if cls.__name__ == 'Rectangle':
                    result = csv.DictWriter(f, fieldnames=rectangle_header)
                elif cls.__name__ == 'Square':
                    result = csv.DictWriter(f, fieldnames=square_header)
                result.writeheader()
                result.writerows(data)

    @classmethod
    def load_from_file_csv(cls):
        """Method that deserializes in CSV"""
        filename = "{}.csv".format(cls.__name__)
        instance_list = []
        try:
            with open(filename) as f:
                result = csv.DictReader(f)
                for row in result:
                    row = dict(row)
                    for key in row:
                        row[key] = int(row[key])
                    instance = cls.create(**row)
                    instance_list.append(instance)
        except FileNotFoundError:
            return instance_list
        return instance_list
