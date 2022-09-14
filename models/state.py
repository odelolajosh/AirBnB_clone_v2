#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    # cascade "all, delete" when a `state`` object is marked for
    # deletion,its related `city` objects should also be marked for deletion
    cities = relationship('City', backref="state", cascade="all, delete")
