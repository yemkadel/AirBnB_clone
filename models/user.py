#!/usr/bin/python3
""" This module contains the usr class """
from models.base_model import BaseModel


class User(BaseModel):
    """ This class defines a User """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    #def __str__(self):
    #    return "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)
