#!/usr/bin/python3
"""This module contains code for user class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class handles all attributes of a user and inheirts
    from the BaseModel class
    """
    name = ""