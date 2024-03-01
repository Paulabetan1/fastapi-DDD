from abc import abstractmethod
from typing import cast, Tuple

from app.core.error.joke_exception import JokeNotFoundError
from app.core.use_cases.use_case import BaseUseCase
from app.features.joke.domain.entities.joke_entity import JokeEntity
from app.features.joke.domain.entities.joke_query_model import JokeReadModel
from app.features.joke.domain.repositories.joke_unit_of_work import JokeUnitOfWork


class DeletejokeUseCase(BaseUseCase):
    unit_of_work: JokeUnitOfWork

    @abstractmethod
    def __call__(self, args: Tuple[int]) -> JokeReadModel:
        raise NotImplementedError()


class DeletejokeUseCaseImpl(DeletejokeUseCase):

    def __init__(self, unit_of_work: JokeUnitOfWork):
        self.unit_of_work: JokeUnitOfWork = unit_of_work

    def __call__(self, args: Tuple[int]) -> JokeReadModel:
        id_, = args

        existing_user = self.unit_of_work.repository.find_by_id(id_)

        if existing_user is None:
            raise JokeNotFoundError()

        marked_joke = existing_user.mark_entity_as_deleted()

        try:
            deleted_user = self.unit_of_work.repository.update(marked_joke)
            self.unit_of_work.commit()
        except Exception:
            self.unit_of_work.rollback()
            raise

        return JokeReadModel.from_entity(cast(JokeEntity, deleted_user))
