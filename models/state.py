#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    # cascade "all, delete" when a `state`` object is marked for
    # deletion,its related `city` objects should also be marked for deletion
    if getenv("HBNB_TYPE_STORAGE") == "db":  # is DB is in use?
        cities = relationship('City', backref="state",
                              cascade="all, delete, delete-orphan")
    else:  # use a property for file storage
        @property
        def cities(self):
            """ cities implementation for `file` storage type """
            all_cities = models.storage.all(City)
            _cities = []
            for city in all_cities:
                if city.state_id == self.id:
                    _cities.append(city)
            return _cities
