#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
import os
from models.base_model import BaseModel



class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}


    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        objcls_name = obj.__class__.__name__
        key = ["{}.{}".format(objcls_name, obj.id)]
        FileStorage.__objects[key] = obj

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        al_obj = FileStorage.__objects
        obj_dict = {}
        for obj in al_obj.keys():
            with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
                json.dump(obj_dict, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as file:
                obj_dict = json.load(file)
                for key in obj_dict.values():
                    cls_name = key["__class__"]
                    del key["__class__"]
                    self.new(eval(cls_name)(**key))
        except FileNotFoundError:
            return
