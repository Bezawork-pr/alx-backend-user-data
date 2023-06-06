#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Query
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql import text
from sqlalchemy.exc import InvalidRequestError


from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add user"""
        _user = User(email=email, hashed_password=hashed_password)
        self._session.add(_user)
        self._session.commit()
        return _user

    def find_user_by(self, **kwargs) -> User:
        """Find user by arg passed"""
        if kwargs is None:
            raise InvalidRequestError
        ur_c = ['id', 'email', 'hashed_password', 'session_id', 'reset_token']
        for arg in kwargs:
            if arg not in ur_c:
                raise InvalidRequestError
        user = self._session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """method will use find_user_by to locate the user to update
        then Update"""
        user = self.find_user_by(id=user_id)
        ur_c = ['id', 'email', 'hashed_password', 'session_id', 'reset_token']
        for key, value in kwargs.items():
            if key not in ur_c:
                raise ValueError
            else:
                user.key = value
        return None
