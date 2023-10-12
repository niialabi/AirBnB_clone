#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods for other classes:"""

from uuid import uuid4
from datetime import datetime
import time


class BaseModel():
    """
    Base Class containing all attributes/methods for other classes
    """
    def __init__(self):
        """
        class instatiation

        Args:
            id: uniq_id of obj

        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        string rep of BaseModel Object
        """
        return("[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__))

    def save(self):
        """
        updates the public instance attribute  the current datetime
        """
        self.updated_at = datetime.now()
        return self

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = type(self).__name__
        dict_copy["created_at"] = dict_copy["created_at"].isoformat()
        dict_copy["updated_at"] = dict_copy["updated_at"].isoformat()
        return dict_copy
