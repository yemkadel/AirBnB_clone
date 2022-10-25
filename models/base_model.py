#!/usr/bin/python3
import uuid
from datetime import datetime
""" This is the base model Module """


class BaseModel:
    """ This is the BaseModel class definition """

    def __init__(self, *args, **kwargs):
        """ This is the constructor of the BaseModel class """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = str(uuid.uuid4())
                elif key == "my_number":
                    self.my_number = value
                elif key == "name":
                    self.name = value
                elif key == "created_at":
                    self.created_at = datetime.now()
                elif key == "updated_at":
                    self.updated_at = self.created_at

    def __str__(self):
        """ returns a str representation of this class """
        return "[{}] ({}) {}".format(__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        This method updates the public instribute
        `updated_at` with the datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        This method returns a dictionary key/value
        of `__dict__` of this instance
        """
        class_dict = self.__dict__
        class_dict["__class__"] = __class__.__name__
        class_dict["created_at"] = self.created_at.isoformat()
        class_dict["updated_at"] = self.updated_at.isoformat()
        return class_dict
