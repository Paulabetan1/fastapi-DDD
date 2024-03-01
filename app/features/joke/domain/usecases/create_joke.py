from abc import abstractmethod
from typing import Tuple

from app.core.use_cases.use_case import BaseUseCase
from app.features.joke.domain.entities.joke_command_model import JokeCreateModel
from app.features.joke.domain.entities.joke_entity import JokeEntity
from app.features.joke.domain.entities.joke_query_model import JokeReadModel
from app.features.joke.domain.repositories.joke_unit_of_work import JokeUnitOfWork


class CreatejokeUseCase(BaseUseCase[Tuple[JokeCreateModel], JokeReadModel]):

    unit_of_work: JokeUnitOfWork

    @abstractmethod
    def __call__(self, args: Tuple[JokeCreateModel]) -> JokeReadModel:
        raise NotImplementedError()


class CreatejokeUseCaseImpl(CreatejokeUseCase):

    def __init__(self, unit_of_work: JokeUnitOfWork):
        self.unit_of_work = unit_of_work

    def __call__(self, args: Tuple[JokeCreateModel]) -> JokeReadModel:
        data, = args

        joke = JokeEntity(
            id_=None,
            **data.dict()
        )

        try:
            self.unit_of_work.repository.create(joke)
        except Exception as _e:
            self.unit_of_work.rollback()
            raise

        self.unit_of_work.commit()

        created_joke = self.unit_of_work.repository.find_by_owner_id(joke.owner_id)[0]

        return JokeReadModel.from_entity(created_joke)
