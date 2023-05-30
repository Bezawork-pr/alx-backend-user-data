#!/usr/bin/env python3
"""This file contains class Auth"""
from flask import request
from typing import List, TypeVar


class Auth:
    """class Auth"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require auth"""
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        for i in excluded_paths:
            if i[-1] != "/":
                i += "/"
        if path[-1] != "/":
            path += "/"
        if path not in excluded_paths or path is None:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user"""
        return None
