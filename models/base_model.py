#!/usr/bin/python3
"""
Module: Base
base_models.py - other classes may inherit from this Base Model class
"""
import json


class BaseModel:
    """ Class: Blase """
    def __init__(self, id=uuid):
        """ Initialization method """
        if hasattr(self, "created_at") and type(self.created_at) is str:
            self.created_at = datetime
        if hasattr(self, "updated_at") and type(self.updated_at) is str:
            self.updated_at = datetime
        else:
            self.id = str(uuid.uud4())
            self.created_at = datetime
            self.updated_at = datetime
