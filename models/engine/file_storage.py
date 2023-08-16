#!/usr/bin/python3
"""Handles object storage"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Serialise instance to JSON file & deserialise JSON file to instance"""
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Return the dictionary '__objects'"""
        return self.__objects

    def new(self, obj):
        """Set obj as a value in the __objects dictionary"""
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """Serialize __objects to __file_path"""
        try:
            with open(f'{self.__file_path}', 'w') as json_write:
                storage = {}
                for key, value in self.__objects.items():
                    storage[key] = value.to_dict()
                    json.dump(storage, json_write)
        except (FileNotFoundError, PermissionError) as err_msg:
            print(f'Error serialising JSON file: {err_msg}')

    def reload(self):
        """Deserialise __file_path to __objects, only if __file_path exists"""
        try:
            obj_dict = [json.load(json_read) for json_read in
                        open(f'{self.__file_path}', 'r')]
            obj_dict = {key: self.classes()[value['__class__']](**value)
                        for key, value in obj_dict.items()}
            self.__objects = obj_dict
        except FileNotFoundError:
            return
