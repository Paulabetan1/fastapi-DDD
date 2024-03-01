from abc import abstractmethod
from typing import Sequence

from app.core.use_cases.use_case import BaseUseCase
from app.features.page.domain.entities.page_query_model import PageReadModel
from app.features.page.domain.services.page_query_service import PageQueryService


class GetPagesUseCase(BaseUseCase[None, Sequence[PageReadModel]]):

    service: PageQueryService

    @abstractmethod
    def __call__(self, args: None) -> Sequence[PageReadModel]:
        raise NotImplementedError()


class GetPagesUseCaseImpl(GetPagesUseCase):

    def __init__(self, service: PageQueryService):
        self.service: PageQueryService = service

    def __call__(self, args: None) -> Sequence[PageReadModel]:
        try:
            pages = self.service.findall()
        except Exception:
            raise

        return pages