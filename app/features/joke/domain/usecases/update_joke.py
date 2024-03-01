from abc import abstractmethod
from typing import cast, Callable, Tuple

from app.core.error.joke_exception import JokeNotFoundError
from app.core.use_cases.use_case import BaseUseCase
from app.features.joke.domain.entities.joke_command_model import JokeUpdateModel
from app.features.joke.domain.entities.joke_entity import JokeEntity
from app.features.joke.domain.entities.joke_query_model import JokeReadModel
from app.features.joke.domain.repositories.joke_unit_of_work import JokeUnitOfWork


class UpdatejokeUseCase(BaseUseCase[Tuple[int, JokeUpdateModel], JokeReadModel]):

    unit_of_work: JokeUnitOfWork

    @abstractmethod
    def __call__(self, args: Tuple[int, JokeUpdateModel]) -> JokeReadModel:
        raise NotImplementedError()


class UpdatejokeUseCaseImpl(UpdatejokeUseCase):

    def __init__(self, unit_of_work: JokeUnitOfWork):
        self.unit_of_work = unit_of_work

    def __call__(self, args: Tuple[int, JokeUpdateModel]) -> JokeReadModel:
        id_, update_data = args
        existing_joke = self.unit_of_work.repository.find_by_id(id_)

        if existing_joke is None:
            raise JokeNotFoundError()

        update_entity = existing_joke.update_entity(
            update_data,
            lambda joke_data: joke_data.dict(exclude_unset=True)
        )

        try:
            updated_joke = self.unit_of_work.repository.update(update_entity)
            self.unit_of_work.commit()
        except Exception:
            self.unit_of_work.rollback()
            raise


        return JokeReadModel.from_entity(cast(JokeEntity, updated_joke))
