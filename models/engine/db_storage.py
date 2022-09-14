#!/usr/bin/python3
"""This module defines a class to manage DB storage for hbnb clone"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        """ Initialize DB storage """
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST", "localhost")
        db = getenv("HBNB_MYSQL_DB")
        __test__ = getenv("HBNB_ENV") == "test"
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(user, passwd, host, db),
            pool_pre_ping=True
        )
        if __test__:  # drop all tables in test mode
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ return all objects depending of the class name """
        _all = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls).all()
            for row in query:
                key = "{}.{}".format(row.__class__.__name__, row.id)
                _all[key] = row
        else:
            classes = User, State, City, Amenity, Place, Review
            for cls in classes:
                query = self.__session.query(cls)
                for row in query:
                    key = "{}.{}".format(row.__class__.__name__, row.id)
                    _all[key] = row
        return _all

    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj):
        """ delete from the current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Loads table and database session """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory=session_factory)
        self.__session = Session()
