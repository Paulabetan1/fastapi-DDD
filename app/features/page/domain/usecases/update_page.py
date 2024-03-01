from abc import abstractmethod
from typing import cast, Tuple, Optional

from app.core.error.page_exception import PageNotFoundError
from app.core.use_cases.use_case import BaseUseCase
from app.features.page.domain.entities.page_command_model import PageUpdateModel
from app.features.page.domain.entities.page_entity import PageEntity
from app.features.page.domain.entities.page_query_model import PageUpdateModel
from app.features.page.domain.repositories.page_unit_of_work import PageUnitOfWork


class UpdatePageUseCase(BaseUseCase[Tuple[int, PageUpdateModel], PageUpdateModel]):
    unit_of_work: PageUnitOfWork

    @abstractmethod
    def __call__(self, args: Tuple[int, PageUpdateModel]) -> PageUpdateModel:
        raise NotImplementedError()


class UpdatePageUseCaseImpl(UpdatePageUseCase):

    def __init__(self, unit_of_work: PageUnitOfWork):
        self.unit_of_work = unit_of_work

    def __call__(self, args: Tuple[int, PageUpdateModel]) -> PageUpdateModel:
        id_, update_data = args

        existing_page: Optional[PageEntity] = self.unit_of_work.repository.find_by_id(id_)

        if existing_page is None:
            raise PageNotFoundError()

        update_entity = existing_page.update_entity(
            update_data,
            lambda page_data: update_data.dict(exclude_unset=True)
        )

        try:
            updated_page = self.unit_of_work.repository.update(update_entity)
            self.unit_of_work.commit()
        except Exception as e:
            self.unit_of_work.rollback()
            raise

        return PageUpdateModel.from_entity(cast(PageEntity, updated_page))
