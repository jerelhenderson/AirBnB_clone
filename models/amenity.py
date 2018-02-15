#!/usr/bin/python3
"""
Module: Amenity
user.py - user-specific that inherits from BaseClass
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Class 'Amenity' inherits from Class 'BaseModel' """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialization method """
super().__init__(*args, **kwargs)
