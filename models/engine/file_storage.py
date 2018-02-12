#!/usr/bin/python3
'''
Module: File Storage
file_storage.py - serialize instance to JSON file and deserialize JSON files to instance
'''
import json


class FileStorage:
    """ serialize instance to JSON file, deserialize JSON file to instance """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__.id
        self.__objects[key] = obj

    def save(self):
        """ writes JSON string repr. of object """
        new_list = {}
        filename = "{}.json".format(self.__file_path)

        if __objects is None:
            return my_json.write(cls.to_json_string(new_list))
        else:
            with open(filename, "w", encoding="UTF8") as my_json:
                for key in self.__objects
                    new_list.append(self.__objects[key].to_dictionary(objects))
                my_json.write(self.objects[key].to_json_string(new_list))
