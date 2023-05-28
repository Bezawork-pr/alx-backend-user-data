#!/usr/bin/env python3
"""Write a function called filter_datum
that returns the log message obfuscated"""
import re


def filter_datum(fields, redaction, message, separator):
    """Obfuscate log message with the redaction given"""
    for field in fields:
        message = re.sub(f'{field}=.+?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message
