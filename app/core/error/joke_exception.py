"""
    User exceptions
"""
from app.core.error.base_exception import BaseError


class JokeNotFoundError(BaseError):
    message = 'Joke does not exist.'

class JokesNotFoundError(BaseError):
    message = 'Joke does not exist.'

class JokeAlreadyExistsError(BaseError):
    message = 'Joke already exists'

