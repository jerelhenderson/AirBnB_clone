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
        key = "{}.{}".format(obj.__class__.__name__,id)
        self.__objects[key] = obj

    def save(self):
        """ writes JSON string repr. of object """
        new_objs = {}
        filename = "{}".format(self.__file_path)

        with open(filename, "w", encoding="UTF8") as f:
            for key, value in self.__objects.items():
                new_objs[key] = value.to_dict()
            #    new_objs.append(self.__objects[key].to_dict())
            # json_objs.write(self.objects[key].to_json_string(new_objs))
            json.dump(new_objs, f)

    def reload(self):
        """ returns list of instances """
        new_objs = {}
        filename = "{}".format(self.__file_path)

        try:
            with open(filename, "r", encoding="UTF8") as f:
                for key, value in json.load(f).items():
                    self.__objects[key] = eval(value["__class__"](**key))
                    # new_list.append(self.__objects(**key))
                return new_objs
        except:
            return {}
