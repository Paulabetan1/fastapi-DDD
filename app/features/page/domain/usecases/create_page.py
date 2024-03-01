from abc import abstractmethod
from typing import cast, Tuple

from app.core.error.page_exception import PageAlreadyExistsError
from app.core.use_cases.use_case import BaseUseCase
from app.features.page.domain.entities.page_command_model import PageCreateModel
from app.features.page.domain.entities.page_entity import PageEntity
from app.features.page.domain.entities.page_query_model import PageReadModel
from app.features.page.domain.repositories.page_unit_of_work import PageUnitOfWork


class CreatePageUseCase(BaseUseCase[Tuple[PageCreateModel], PageReadModel]):

    unit_of_work: PageUnitOfWork

    @abstractmethod
    def __call__(self, args: Tuple[PageCreateModel]) -> PageReadModel:
        raise NotImplementedError()


class CreatePageUseCaseImpl(CreatePageUseCase):

    def __init__(self, unit_of_work: PageUnitOfWork):
        self.unit_of_work = unit_of_work

    def __call__(self, args: Tuple[PageCreateModel]) -> PageReadModel:
        data, = args

        page = PageEntity(
            id_=None,
            **data.dict()
        )

        existing_page = self.unit_of_work.repository.find_by_email(data.email)
        if existing_page is not None:
            raise PageAlreadyExistsError()

        try:
            self.unit_of_work.repository.create(page)
        except Exception as _e:
            self.unit_of_work.rollback()
            raise

        self.unit_of_work.commit()

        created_page = self.unit_of_work.repository.find_by_email(data.email)

        return PageReadModel.from_entity(cast(PageEntity, created_page))
