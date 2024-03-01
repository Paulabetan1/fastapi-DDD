from datetime import datetime

from pydantic import Field

from app.features.joke.domain.entities.joke_common_model import JokeBaseModel
from app.features.joke.domain.entities.joke_entity import JokeEntity


class JokeReadModel(JokeBaseModel):
    id_: int = Field(example=111)
    is_deleted: bool = Field(example=True)
    created_at: datetime
    updated_at: datetime

    class Config(object):
        orm_mode = True

    @classmethod
    def from_entity(cls, entity: JokeEntity) -> 'JokeReadModel':
        return cls(
            id_=entity.id_,
            title=entity.title,
            owner_id=entity.owner_id,
            is_completed=entity.is_completed,
            is_deleted=entity.is_deleted,
            created_at=entity.created_at,
            updated_at=entity.updated_at
        )
