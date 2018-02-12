#!/usr/bin/python3
"""
Module: Base
base_models.py - other classes may inherit from this Base Model class
"""
import json
from datetime import datetime
import uuid


class BaseModel:
    """ Class: Base """
    def __init__(self):
        '''
        Initializes an instance
        '''
        id = str(uuid.uuid4())
        created_at = datetime.now()
        updated_at = datetime.now()

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
        class_dict = self.__dict__
        class_dict['__class__'] = self.__class__
        class_dict[created_at] = isoformat(created_at)
        class_dict[updated_at] = isoformat(updated_at)
        return class_dict
