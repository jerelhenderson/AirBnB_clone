#!/usr/bin/python3
"""
Module: State
user.py - user-specific that inherits from BaseClass
"""
from models.base_model import BaseModel
import models


class State(BaseModel):
    """ Class 'State' inherits from Class 'BaseModel' """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
