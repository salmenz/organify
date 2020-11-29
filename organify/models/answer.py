#!/usr/bin/python3
"""
Class Answer
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship


class Answer(BaseModel, Base):
    """
    Representation of an answer
    """
    __tablename__ = 'Answer'
    content = Column(String(255), nullable=True)
    u_id = Column(String(60), ForeignKey('Users.id'), nullable=False)
    quest_id = Column(String(60), ForeignKey('Question.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
