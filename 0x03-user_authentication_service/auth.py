#!/usr/bin/env python3
"""Define a _hash_password method
that takes in a password string arguments"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """takes in a password string arguments
    and returns bytes"""
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    return hash
