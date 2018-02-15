#!/usr/bin/python3
"""
Module: Place
user.py - user-specific that inherits from BaseClass
"""
from models.base_model import BaseModel
import models


class Place(BaseModel):
    """ Class 'Place' inherits from Class 'BaseModel' """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
