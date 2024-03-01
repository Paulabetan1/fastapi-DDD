from pydantic import BaseModel, Field

from app.core.error.joke_exception import JokeNotFoundError, JokesNotFoundError


class ErrorMessageJokeNotFound(BaseModel):
    detail: str = Field(example=JokeNotFoundError.message)


class ErrorMessageJokesNotFound(BaseModel):
    detail: str = Field(example=JokesNotFoundError.message)

