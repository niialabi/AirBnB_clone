#!/usr/bin/python3
"""Class review that inherit from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):

    place_id = ""
    user_id = ""
    text = ""
