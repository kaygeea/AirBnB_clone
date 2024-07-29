"""
Module containing the BaseModel class.

The BaseModel class serves as a base for other classes, providing
common attributes and methods for managing instance identification,
creation, update timestamps, and serialization to dictionary format.
"""

from datetime import datetime, timezone
from uuid import uuid4

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
    
    def __init__(self, *args, **kwargs) -> None:
        """
        Initialize a new instance of BaseModel.

        Creates a unique identifier and sets the creation and update
        timestamps to the current time.
        """
        if kwargs:
            for att_name, att_val in kwargs.items():
                if att_name != "__class__":
                    setattr(self, att_name, att_val)
            if 'created_at' in kwargs and isinstance(kwargs['created_at'], str):
                self.created_at = datetime.fromisoformat(kwargs['created_at'])
            if 'updated_at' in kwargs and isinstance(kwargs['updated_at'], str):
                self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now(timezone.utc)
            self.updated_at = datetime.now(timezone.utc)

    def __str__(self):
        """
        Return a string representation of the instance.

        The string includes the class name, unique identifier, and
        dictionary of the instance's attributes.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    def save(self):
        """
        Update the instance's update timestamp.

        Sets the 'updated_at' attribute to the current time.
        """
        self.updated_at = datetime.now(timezone.utc)

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