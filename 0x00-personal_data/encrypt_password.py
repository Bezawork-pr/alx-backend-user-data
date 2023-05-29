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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Use bcrypt to validate that the provided
    password matches the hashed password"""
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        return True
    return False
