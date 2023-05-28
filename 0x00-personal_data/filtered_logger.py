#!/usr/bin/env python3
"""Write a function called filter_datum
that returns the log message obfuscated"""
import re
import os
from typing import List
import logging
import mysql.connector
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Instantiate class and super class"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Use function filter_datum to filter"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Obfuscate log message with the redaction given"""
    for field in fields:
        message = re.sub(f'{field}=.+?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message


def get_logger() -> logging.Logger:
    """returns a logging.Logger object"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger


def get_db()-> mysql.connector.connection.MySQLConnection:
    """Returns a connector to the database"""
    return mysql.connector.connect(host=os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost'),
                                    database=os.environ.get('PERSONAL_DATA_DB_NAME'),
                                    user=os.environ.get('PERSONAL_DATA_DB_USERNAME'),
                                    password=os.environ.get('PERSONAL_DATA_DB_PASSWORD', "")
                                    )
    
