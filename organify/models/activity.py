#!/usr/bin/python3
"""
Class activity
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship


class Activity(BaseModel, Base):
    """
    Representation of an Activity
    """
    __tablename__ = 'Activity'
    status = Column(String(255), nullable=False)
    submit_date = Column(Date, nullable=True)
    type = Column(String(255), nullable=True)
    user_id = Column(String(60), ForeignKey('Users.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
