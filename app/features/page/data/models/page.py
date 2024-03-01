from typing import TYPE_CHECKING

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, Mapped

from app.features.page.domain.entities.page_query_model import PageReadModel
from app.core.models.postgres.models import Base
from app.features.page.domain.entities.page_entity import PageEntity

if TYPE_CHECKING:
    from app.features.joke.data.models.joke import Joke


class Page(Base):
    """
        page DTO is an object associated with page entity USEEEER
    """
    __tablename__ = 'pages'

    url: Mapped[int] | int = Column(int, unique=True, index=True)
    name: Mapped[str] | str = Column(String)

    jokes: Mapped[list['Joke']] = relationship('Joke', back_populates='jokes', uselist=True)

    def to_entity(self) -> PageEntity:
        return PageEntity(
            id_=self.id_,
            url=self.url,
            name=self.name,
            created_at=self.created_at,
            updated_at=self.updated_at,
            is_deleted=self.is_deleted,
            jokes=[joke.id_ for joke in self.jokes]
        )

    def to_dict(self):
        return {
            'id_': self.id_,
            'url': self.url,
            'name': self.name,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'is_deleted': self.is_deleted,
        }

    def to_read_model(self) -> PageReadModel:
        return PageReadModel(
            id_=self.id_,
            url=self.url,
            name=self.name,
            is_deleted=self.is_deleted,
            created_at=self.created_at,
            updated_at=self.updated_at,
            jokes=[joke.id_ for joke in self.jokes]
        )

    @staticmethod
    def from_entity(page: PageEntity) -> 'Page':
        return page(
            id_=page.id_,
            url=page.url,
            name=page.name,
            created_at=page.created_at,
            updated_at=page.updated_at,
            is_deleted=page.is_deleted
        )
