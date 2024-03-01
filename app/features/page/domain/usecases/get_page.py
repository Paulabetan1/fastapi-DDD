from abc import abstractmethod
from typing import Tuple

from app.core.use_cases.use_case import BaseUseCase
from app.features.page.domain.entities.page_query_model import PageReadModel
from app.features.page.domain.services.page_query_service import PageQueryService
from app.core.error.page_exception import PageNotFoundError


class GetPageUseCase(BaseUseCase[Tuple[int], PageReadModel]):
    """
        GetpageUseCase defines a query use case interface related page Entity
    """

    service: PageQueryService

    @abstractmethod
    def __call__(self, args: Tuple[int]) -> PageReadModel:
        raise NotImplementedError()


class GetPageUseCaseImpl(GetPageUseCase):
    """
        GetpageUseCaseImpl implements a query use cases related to page entity
    """

    def __init__(self, service: PageQueryService):
        self.service: PageQueryService = service

    def __call__(self, args: Tuple[int]) -> PageReadModel:
        id_, = args

        try:
            page = self.service.find_by_id(id_)
            if page is None:
                raise PageNotFoundError()
        except Exception:
            raise

        return page

