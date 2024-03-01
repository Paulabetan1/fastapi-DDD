"""
    User exceptions
"""
from app.core.error.base_exception import BaseError


class PageNotFoundError(BaseError):
    message = 'Joke does not exist.'

class PagesNotFoundError(BaseError):
    message = 'Joke does not exist.'

class PageAlreadyExistsError(BaseError):
    message = 'Joke already exists'

