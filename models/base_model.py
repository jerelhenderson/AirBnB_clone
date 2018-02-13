 #!/usr/bin/python3
"""
Module: Base
base_models.py - other classes may inherit from this Base Model class
"""
import json
import models
import uuid
from datetime import date
from datetime import datetime


class BaseModel:
    """ Class: Base """
    def __init__(self, *args, **kwargs):
        ''' initialize instance '''
        if kwargs:
            for key, value in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, value)

            self.created_at = datetime.strptime(self.created_at,
                                                "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(self.updated_at,
                                                "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def save(self):
        ''' updates updated_at attribute '''
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        ''' print string '''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def to_dict(self):
        ''' returns dictionary containing all keys/values of __dict__ '''
        c_d = self.__dict__.copy()
        c_d['__class__'] = self.__class__.__name__
        c_d['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        c_d['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return c_d
