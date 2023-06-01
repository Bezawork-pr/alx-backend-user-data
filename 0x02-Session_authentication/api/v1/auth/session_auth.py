#!/usr/bin/env python3
"""class SessionAuth"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """SessionAuth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a Session ID for a user_id"""
        if user_id is None:
            return None
        if type(user_id) != str:
            return None
        id = str(uuid.uuid4())
        self.user_id_by_session_id[id] = user_id
        return id

    def user_id_for_session_id(self,
                               session_id: str = None) -> str:
        """ a User ID based on a Session ID"""
        if session_id is None:
            return None
        if type(session_id) != str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Returns a User instance based on a cookie value"""
        session_cookie = self.session_cookie(request)
        try:
            user_id = self.user_id_by_session_id[session_cookie]
            return User.get(user_id)
        except Exception as NotFound:
            return None
