#!/usr/bin/python3
"""
Module: City
user.py - user-specific that inherits from BaseClass
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ Class 'City' inherits from Class 'BaseModel' """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialization method """
super().__init__(*args, **kwargs)
