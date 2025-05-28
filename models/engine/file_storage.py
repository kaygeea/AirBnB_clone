#!/usr/bin/python3
"""
Module containing the FileStorage class.

The FileStorage class serializes instances to a JSON file and 
deserializes JSON file to instances.
"""
from json import dump, load
from pathlib import Path

class FileStorage:
    """
    Class for serializing instances to a JSON file and deserializing
    JSON file to instances.

    Private class attributes:
    - __file_path: string - path to the JSON file (ex: file.json)
    - __objects: dictionary - empty but will store all objects by
      <class name>.id (ex: to store a BaseModel object with id=12121212,
      the key will be BaseModel.12121212)

    Public instance methods:
    - all(self): returns the dictionary __objects
    - new(self, obj): sets in __objects the obj with key <obj class name>.id
    - save(self): serializes __objects to the JSON file (path: __file_path)
    - reload(self): deserializes the JSON file to __objects (only if the
      JSON file (__file_path) exists; otherwise, do nothing)
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return the dictionary __objects.

        Returns:
            dict: A dictionary containing all stored objects.
        """
        return self.__objects
    
    def new(self, obj):
        """
        Set in __objects the obj with key <obj class name>.id.

        Args:
            obj (BaseModel): The object to store in the dictionary.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj.to_dict()

    def save(self):
        """Serializes __objects to the JSON file at __file_path."""
        with open(self.__file_path, 'w') as f:
            dump(self.__objects, f, indent=4)

    def reload(self):
        """
        Deserialize the JSON file to __objects.

        Loads the JSON file content into the __objects dictionary if the
        file exists.
        """
        if Path(self.__file_path).exists():
            with open(self.__file_path) as data:
                self.__objects = load(data)
        else:
            pass
