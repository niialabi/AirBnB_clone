#!/usr/bin/python3
"""user class inherits from basemodels"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Attribute of the user are{
    email: string - empty string
    password: string - empty string
    first_name: string - empty string
    last_name: string - empty string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
