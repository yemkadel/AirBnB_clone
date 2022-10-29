#!/usr/bin/python3
""" This is the base model module """
import uuid
from datetime import datetime
import models


class BaseModel:
    """ This is the BaseModel class definition """

    def __init__(self, *args, **kwargs):
        """ This is the constructor of the BaseModel class """
        tformat = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, tformat)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """ returns a str representation of this class """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        This method updates the public instribute
        `updated_at` with the datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        This method returns a dictionary key/value
        of `__dict__` of this instance
        """
        class_dict = self.__dict__
        class_dict["__class__"] = self. __class__.__name__
        class_dict["created_at"] = self.created_at.isoformat()
        class_dict["updated_at"] = self.updated_at.isoformat()
        return class_dict
