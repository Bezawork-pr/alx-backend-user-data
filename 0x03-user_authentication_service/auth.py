#!/usr/bin/env python3
"""Define a _hash_password method
that takes in a password string arguments"""
import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """takes in a password string arguments
    and returns bytes"""
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    return hash


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
            user = self._db.add_user(email=email, hashed_password=hashed_password)
            return user
        else:
            raise ValueError(f"User {email} already exists")
