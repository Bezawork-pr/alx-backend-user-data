#!/usr/bin/env python3
"""This file contains class BasicAuth"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """class BasicAuth"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str
                                            ) -> str:
        """Return Base 64"""
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        if authorization_header.startswith("Basic ") is False:
            return None
        return authorization_header[6:]
