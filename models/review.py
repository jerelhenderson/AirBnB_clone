#!/usr/bin/python3
"""
Module: Review
user.py - user-specific that inherits from BaseClass
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Class 'Review' inherits from Class 'BaseModel' """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ Initialization method """
        super().__init__(*args, **kwargs)
