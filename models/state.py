#!/usr/bin/python3
"""
Module: State
user.py - user-specific that inherits from BaseClass
"""
from models.base_model import BaseModel


class State(BaseModel):
    """ Class 'State' inherits from Class 'BaseModel' """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ Initialization method """
        super().__init__(*args, **kwargs)
