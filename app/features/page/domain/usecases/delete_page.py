from abc import abstractmethod
from typing import cast, Tuple

from app.core.error.page_exception import PageNotFoundError
from app.features.page.domain.entities.page_entity import PageEntity
from app.features.page.domain.entities.page_query_model import PageReadModel
from app.features.page.domain.repositories.page_unit_of_work import PageUnitOfWork
from app.core.use_cases.use_case import BaseUseCase


class DeletePageUseCase(BaseUseCase[Tuple[int], PageReadModel]):
    """
        pageCommandUseCase defines a command use case interface related page entity
    """
    unit_of_work: PageUnitOfWork

    @abstractmethod
    def __call__(self, args: Tuple[int]) -> PageReadModel:
        raise NotImplementedError()


class DeletePageUseCaseImpl(DeletePageUseCase):
    """
        pageCommandUseCaseImpl implements a command use cases related to the page entity
    """

    def __init__(self, unit_of_work: PageUnitOfWork):
        self.unit_of_work: PageUnitOfWork = unit_of_work

    def __call__(self, args: Tuple[int]) -> PageReadModel:
        id_, = args
        existing_page = self.unit_of_work.repository.find_by_id(id_)

        if existing_page is None:
            raise PageNotFoundError()

        marked_page = existing_page.mark_entity_as_deleted()

        try:
            deleted_page = self.unit_of_work.repository.update(marked_page)
            self.unit_of_work.commit()
        except Exception as e:
            self.unit_of_work.rollback()
            raise

        return PageReadModel.from_entity(cast(PageEntity, deleted_page))
