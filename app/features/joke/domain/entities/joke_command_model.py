from pydantic import Field

from app.features.joke.domain.entities.joke_common_model import JokeBaseModel


class JokeCreateModel(JokeBaseModel):
    pass


class JokeUpdateModel(JokeBaseModel):
    is_completed: bool = Field(example=True)
    is_deleted: bool = Field(example=True)