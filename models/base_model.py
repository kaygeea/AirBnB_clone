#!/usr/bin/python3

"""
Module containing the BaseModel class.

The BaseModel class serves as a base for other classes, providing
common attributes and methods for managing instance identification,
creation, update timestamps, and serialization to dictionary format.
"""

from uuid import uuid4
from datetime import datetime
from . import storage

class BaseModel:
    """
    Base class for all models, providing common functionality.

    Public Methods:
    - save: Updates the instance's update timestamp.
    - to_dict: Serializes the instance to a dictionary.

    Instance Variables:
    - id: Unique identifier for the instance.
    - created_at: Timestamp when the instance was created.
    - updated_at: Timestamp when the instance was last updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of BaseModel.

        Creates a unique identifier and sets the creation and update
        timestamps to the current time. If kwargs are provided, the
        instance is initialized from the dictionary representation.
        Otherwise, it is considered a new instance and added to storage.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key in kwargs.keys():
                if key != "__class__":
                    value = ""

                    if key == "created_at" or key == "updated_at":
                        value = datetime.fromisoformat(kwargs[key])
                    else:
                        value = kwargs[key]
                    setattr(self, key, value)

    def __str__(self):
        """
        Return a string representation of the instance.

        The string includes the class name, unique identifier, and
        dictionary of the instance's attributes.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """
        Set the `updated_at` instance attribute to the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Serialize the instance to a dictionary.

        The dictionary includes all instance attributes, the class name,
        and the ISO-formatted timestamps for 'created_at' and 'updated_at'.

        Returns:
            dict: A dictionary representation of the instance.
        """

        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = instance_dict["created_at"].isoformat()
        instance_dict["updated_at"] = instance_dict["updated_at"].isoformat()

        return instance_dict
