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

    def __init__(self):
        """
        Initialize a new instance of FileStorage.

        This method doesn't require any parameters and initializes the
        storage engine.
        """
        pass

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
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj
    
    def save(self):
        """
        Set in __objects the obj with key <obj class name>.id.

        Args:
            obj (BaseModel): The object to store in the dictionary.
        """
        with open(self.__file_path, "w") as file:
            dump(self.__objects, file)

    def reload(self):
        """
        Deserialize the JSON file to __objects.

        Loads the JSON file content into the __objects dictionary if the
        file exists.
        """
        if Path(self.__file_path).is_file():
            with open(self.__file_path) as data:
                self.__objects = load(data)
