from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped

from app.core.models.postgres.models import Base
from app.features.joke.domain.entities.joke_entity import JokeEntity
from app.features.joke.domain.entities.joke_query_model import JokeReadModel

if TYPE_CHECKING:
    from app.features.page.data.models.page import Page


class Joke(Base):
    """
        Task DTO is an object associated with user entity taaaskk
    """
    __tablename__ = 'jokes'

    text: Mapped[str] | str = Column(String, index=True)
    owner_id: Mapped[int] | int = Column(Integer, ForeignKey('page.id_'))

    owner: Mapped['Page'] = relationship('Page', back_populates='pages', uselist=False)

    def to_entity(self) -> JokeEntity:
        return JokeEntity(
            id_=self.id_,
            text=self.text,
            is_deleted=self.is_deleted,
            owner_id=self.owner_id,
            updated_at=self.updated_at,
            created_at=self.created_at
        )

    def to_read_model(self) -> JokeReadModel:
        return JokeReadModel(
            id_=self.id_,
            text=self.text,
            is_deleted=self.is_deleted,
            owner_id=self.owner_id,
            updated_at=self.updated_at,
            created_at=self.created_at
        )

    def to_dict(self):
        return {
            'id_': self.id_,
            'text': self.text,
            'owner_id': self.owner_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'is_deleted': self.is_deleted,
        }

    @staticmethod
    def from_entity(task: JokeEntity) -> 'Joke':
        return Joke(
            id_=task.id_,
            text=task.text,
            is_deleted=task.is_deleted,
            owner_id=task.owner_id,
            updated_at=task.updated_at,
            created_at=task.created_at
        )
