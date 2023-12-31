#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods for other classes:"""

from uuid import uuid4
from datetime import datetime
import time


class BaseModel():
    """
    Base Class containing all attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        class instatiation

        Args:
            *args: uniq_id of obj(not used in implementation)
            **kwargs: dict of args(create insatance from dict)

        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        date_format = "%Y-%m-%dT%H:%M:%S.%f"
                        setattr(self, key,
                                datetime.strptime(value, date_format))
                    elif key == "id":
                        setattr(self, key, str(value))
                    else:
                        setattr(self, key, value)
        if not kwargs:
            from models import storage
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

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
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = type(self).__name__
        dict_copy["created_at"] = dict_copy["created_at"].isoformat()
        dict_copy["updated_at"] = dict_copy["updated_at"].isoformat()
        return dict_copy
