#!/usr/bin/python3
"""
Module: Amenity
user.py - user-specific that inherits from BaseClass
"""
from models.base_model import BaseModel
import models


class Amenity(BaseModel):
    """ Class 'Amenity' inherits from Class 'BaseModel' """
    name = ""
