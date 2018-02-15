#!/usr/bin/python3
"""
Module: City
user.py - user-specific that inherits from BaseClass
"""
from models.base_model import BaseModel
import models


class City(BaseModel):
    """ Class 'City' inherits from Class 'BaseModel' """
    state_id = ""
    name = ""
