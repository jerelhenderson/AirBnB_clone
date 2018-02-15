#!/usr/bin/python3
"""
Module: User
user.py - user-specific that inherits from BaseClass
"""
from models.base_model import BaseModel
import models


class User(BaseModel):
    """ Class 'User' inherits from Class 'BaseModel' """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
