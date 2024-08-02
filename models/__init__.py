"""
Initialize the models package.

This module creates a unique FileStorage instance for the application
and reloads any previously stored data.

Attributes:
    storage (FileStorage): An instance of FileStorage used to manage
    serialization and deserialization of all models.
"""

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()