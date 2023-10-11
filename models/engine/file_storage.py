#!/usr/bin/python3
import json
from models.base_model import BaseModel
"""Defines a Storage class"""


class FileStorage:
    """Represents an abstracted storage engine"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        ob_dict = {k: o.to_dict() for k, o in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(ob_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path) as f:
                ob_dict = json.load(f)
                for key, val in ob_dict.items():
                    class_name = val['__class__']
                    del val['__class__']
                    obj = eval(class_name)(**val)
                    self.new(obj)
        except FileNotFoundError:
            return
