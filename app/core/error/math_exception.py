"""
    Task Exceptions
"""
from app.core.error.base_exception import BaseError


class NotFoundError(BaseError):
    message = 'Task does not exist.'


class IsNotNumber(BaseError):
    message = 'The input is not a number'

