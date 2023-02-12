#!/usr/bin/python3
"""define the FileStrorage class."""

import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects"""
        FileStorage.__objects["{}.{}".format(obj.__class__.__name, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        fs = FileStorage.__objects
        wr_what = {obj: fs[obj].to_dict() for obj in fs.keys()}
        with open(FileStorage.__file_path, "w") as fp:
            json.dump(wr_what, fp)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path) as fp:
                my_dict = json.load(fp)
                for x in my_dict.values():
                    cls_name = x["__class__"]
                    del x["__class__"]
                    self.new(eval(cls_name)(**x))
        except FileNotFoundError:
            return
