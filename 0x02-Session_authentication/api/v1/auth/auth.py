#!/usr/bin/env python3
"""This file contains class Auth"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """class Auth"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require auth"""
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        for i in excluded_paths:
            if i[-1] != "/":
                i += "/"
        for i in excluded_paths:
            if i[-2] != "*":
                if path.startswith(i[:-3]):
                    return False
                else:
                    return True
        if path[-1] != "/":
            path += "/"
        if path not in excluded_paths or path is None:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """authorization header"""
        if request is None:
            return None
        if not request.headers.get("Authorization"):
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user"""
        return None

    def session_cookie(self, request=None):
        """returns a cookie value from a request"""
        if request is None:
            return None
        session_name = getenv('SESSION_NAME')
        return request.cookies.get(session_name)
