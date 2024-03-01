from abc import abstractmethod

from app.core.repositories.base_repository import BaseRepository
from app.features.page.domain.entities.page_entity import PageEntity


class PageRepository(BaseRepository[PageEntity]):
    """pageRepository defines a repositories interface for page entity"""

    @abstractmethod
    def find_by_email(self, email: str) -> PageEntity | None:
        raise NotImplementedError()

