#!/usr/bin/env python3
"""Define a _hash_password method
that takes in a password string arguments"""
import bcrypt
from db import DB
from user import User
import bcrypt
import uuid
from typing import Union


def _hash_password(password: str) -> bytes:
    """takes in a password string arguments
    and returns bytes"""
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    return hash


def _generate_uuid() -> str:
    """Generate uuid"""
    id = str(uuid.uuid4())
    return id


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Instantiate class"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register User"""
        try:
            self._db.find_user_by(email=email)
        except Exception as NewUser:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user
        else:
            raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        """Validate Login"""
        try:
            user = self._db.find_user_by(email=email)
        except Exception as NotFound:
            return False
        if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
            return True
        return False

    def create_session(self, email: str) -> Union[str, None]:
        """takes an email string argument
        and returns the session ID as a string."""
        try:
            user = self._db.find_user_by(email=email)
        except Exception as NotFound:
            return None
        session_id = _generate_uuid()
        self._db.update_user(user_id=user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> Union[str, None]:
        """takes a single session_id string argument and
        returns the corresponding User or None"""
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
        except Exception as NotFound:
            return None
        return user

    def destroy_session(self, user_id: int) -> None:
        """ The method takes a single user_id
        integer argument and returns None"""
        self._db.update_user(user_id=user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """Find the user corresponding to the email
        If the user does not exist, raise a ValueError exception
        If it exists, generate a UUID and update
        the user’s reset_token"""
        try:
            user = self._db.find_user_by(email=email)
        except Exception as NotFound:
            raise ValueError
        token = uuid.uuid4()
        self._db.update_user(user_id=user.id, reset_token=token)
