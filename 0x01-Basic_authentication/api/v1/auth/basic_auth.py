#!/usr/bin/env python3
"""This file contains class BasicAuth"""
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """return the decoded value as UTF8 string"""
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) != str:
            return None
        try:
            return base64.b64decode(
                                    base64_authorization_header
                                    ).decode('utf-8')
        except Exception as NotBase64:
            return None
