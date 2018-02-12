#!/usr/bin/python3
"""
Module: Base
base_models.py - other classes may inherit from this Base Model class
"""
import json
from datetime import date
from datetime import datetime
import uuid


class BaseModel:
    """ Class: Base """
    def __init__(self):
        '''
        Initializes an instance
        '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        '''
        Updates the updated_at attribute
        '''
        self.updated_at = datetime.now()

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
        c_d = self.__dict__
        c_d['__class__'] = self.__class__.__name__
        c_d['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        c_d['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return c_d
