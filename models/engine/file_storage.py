#!/usr/bin/python3
""" This is the  File storage module """
import json
from models.base_model import BaseModel


class FileStorage:
    """ This class defines a FileStorage instance """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ The method returns all the __objects dictionary """
        return self.__objects

    def new(self, obj):
        """
        This method adds a new obj in the
        __objects dictionary with key as
        <obj class name>.id
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        This method serializes dictionary __objects
        to a JSON File
        """
        with open(self.__file_path, "w", encoding="utf-8") as f:
            obj_dict = {obj_key: self.__objects[obj_key].to_dict()
                        for obj_key in self.__objects.keys()}
            json.dump(obj_dict, f)

    def delete(self, obj):
        """
        This method deletes an object
        from the __objects dict
        """
        del self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)]

    def reload(self):
        """
        This method deserializes a JSON file to __objects
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for obj in obj_dict.values():
                    cl_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cl_name)(**obj))
        except FileNotFoundError:
            return
