#!/usr/bin/python3
'''
Module: File Storage
Serialize instance to JSON file, deserialize JSON files to instance
'''
import json
import models   

class FileStorage:
    """ serialize instance to JSON file, deserialize JSON file to instance """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ writes JSON string repr. of object """
        new_objs = {}

        for key, value in self.__objects.items():
            new_objs[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(new_objs, f)

    def reload(self):
        """ returns list of instances """
        loaded_dictionary = {}
        try:
            with open(self.__file_path, "r", encoding="UTF8") as f:
                loaded_dictionary = json.load(f)
            for key, value in loaded_dictionary.items():
                x = value.get("__class__")
                if x in models.available_models:
                    self.__objects[key] = models.available_models[x](**value)
        except FileNotFoundError:
            pass
