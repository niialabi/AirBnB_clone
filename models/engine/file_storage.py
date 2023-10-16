#!/usr/bin/python3
"""
Module containe file storage class
"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    class FileStorage that serializes instances to a
     JSON file and deserializes JSON file to instances:
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        func that returns the dictionary objects
        """
        return self.__objects

    def new(self, obj):
        """
        function sets in __objects the obj with key <obj class name>.id

        Args:
            obj: class instance to be set in __objects
        """
        class_name = obj.__class__.__name__
        self.__objects["{}.{}".format(class_name, obj.id)] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        obj_dict_tosave = {}
        for key, value in self.__objects.items():
            obj_dict_tosave[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict_tosave, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                temp = json.load(f)

            for key, value in temp.items():
                class_name = key.split(".")[0]
                obj_reload = eval(class_name)(**value)
                self.new(obj_reload)
        except FileNotFoundError:
            pass
