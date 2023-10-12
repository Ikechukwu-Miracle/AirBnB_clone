#!/usr/bin/python3
"""This module contains code for user class"""
from models.base_model import BaseModel


class State(BaseModel):
    """This State class handles all attributes of a user and inheirts
    from the BaseModel class
    """
    name = ""
