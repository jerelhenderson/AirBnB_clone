 #!/usr/bin/python3
'''
Module: File Storage
file_storage.py - serialize instance to JSON file, deserialize JSON files to instance
'''
import json
from models.base_model import BaseModel


class FileStorage:
    """ serialize instance to JSON file, deserialize JSON file to instance """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__.id)
        self.__objects = self._objects + obj

    def save(self):
        """ writes JSON string repr. of object """
        new_objs = {}
        filename = "{}.json".format(self.__file_path)

        with open(filename, "w", encoding="UTF8") as json_objs:
            for key in self.__objects:
                new_list.append(self.__objects[key].to_dict())
            # json_objs.write(self.objects[key].to_json_string(new_objs))
            return json.dumps(new_objs, filename)

    def reload(self):
        """ returns list of instances """
        new_list = {}
        filename = "{}.json".format(self.__file_path)

        try:
            with open(filename, "r", encoding="UTF8") as json_objs:
                for key in json.load(filename):
                    new_list.append(self.__objects(**key))
                return new_list
        except:
            return {}
