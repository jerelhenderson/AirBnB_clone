#!/usr/bin/python3
"""
Module: Review
user.py - user-specific that inherits from BaseClass
"""
from models.base_model import BaseModel
import models


class Review(BaseModel):
    """ Class 'Review' inherits from Class 'BaseModel' """
    place_id = ""
    user_id = ""
    text = ""
