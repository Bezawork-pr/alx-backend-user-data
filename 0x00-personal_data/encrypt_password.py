#!/usr/bin/env python3
"""Implement a hash_password function that expects one
string argument name password and returns a salted,
hashed password, which is a byte string"""
import bcrypt


def hash_password(password: str) -> bytes:
    """hash password with bcrpt"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed
