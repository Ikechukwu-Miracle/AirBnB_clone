#!/usr/bin/python3
"""Defines BaseModel class"""
import uuid
from datetime import datetime



class BaseModel:
    """Base class for the HBnB project"""

    def __init__(self):
        """Initilizes an instance of the class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all
        keys/values of __dict__ of the instance
        """

        ob_dict = self.__dict__.copy()
        ob_dict['__class__'] = self.__class__.__name__
        ob_dict['created_at'] = self.created_at.isoformat()
        ob_dict['updated_at'] = self.updated_at.isoformat()

        return ob_dict

    def __str__(self):
        """Returns the str representation of the object"""
        class_name = self.__class__.__name__

        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
