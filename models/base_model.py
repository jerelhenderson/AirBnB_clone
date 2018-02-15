#!/usr/bin/python3
'''
Setting up the BaseModel class that other classes can inherit from
'''
import json
import models
import uuid
from datetime import date
from datetime import datetime


class BaseModel:
    """
    Class: Base
    """
    def __init__(self, *args, **kwargs):
        '''
        Initializes an instance
        '''
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
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
        models.storage.save()

    def save(self):
        '''
        Updates the updated_at attribute
        '''
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def __str__(self):
        '''
        Prints a string
        '''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def to_dict(self):
        '''
        Returns a dictionary containing all keys/values of __dict__
        '''
        c_d = self.__dict__.copy()
        c_d['__class__'] = self.__class__.__name__
        c_d['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        c_d['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return c_d

    def __repr__(self):
        '''
        Sets the repr
        '''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)
