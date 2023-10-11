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
        self.created_at = str(datetime.now().isoformat())
        self.updated_at = str(datetime.now().isoformat())

    def __str__(self):
        """
        string rep of BaseModel Object
        """
        return("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))
