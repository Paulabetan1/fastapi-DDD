from datetime import datetime

from pydantic import Field

from app.features.page.domain.entities.page_entity import PageEntity
from app.features.page.domain.entities.page_common_model import PageBaseModel


class PageReadModel(PageBaseModel):
    """
        pageReadModel represents data structure as a read model
    """

    id_: int = Field(example=1111)
    url: str = Field(example='test@test.com')
    name: str = Field(example='duck')
    is_deleted: bool = Field(example=True)
    created_at: datetime
    updated_at: datetime
    tasks: list[int]

    class Config:
        orm_mode = True

    @staticmethod
    def from_entity(entity: PageEntity) -> 'PageReadModel':
        return PageReadModel(
            id_=entity.id_,
            url=entity.url,
            name=entity.name,
            is_deleted=entity.is_deleted,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
            tasks=entity.tasks
        )
