#!/usr/bin/python3
"""
Module: User
user.py - user-specific that inherits from BaseClass
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ Class 'User' inherits from Class 'BaseModel' """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ Initialization method """
super().__init__(*args, **kwargs)
