#!/usr/bin/env python3

"""defines a BaseModel class."""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """defines common attributes/methods for use by other classes."""

    def __init__(self, *args, **kwargs):
        """initialization of attributes."""

        fmt = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or "updated_at":
                    self.__dict__[k] = datetime.strptime(v, fmt)
                else:
                    self.__dict__[k] = v

    def save(self):
        """updates the attribute updated_at with the current datetime"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """returns a dict with all keys/values of __dict__ of the instance"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict

    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>"""
        class_name = self.__clas__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
