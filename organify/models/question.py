#!/usr/bin/python3
"""
Class Question
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship


class Question(BaseModel, Base):
    """
    Representation of a Question
    """
    __tablename__ = 'Question'
    content = Column(String(255), nullable=True)
    u_id = Column(String(60), ForeignKey('Users.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
