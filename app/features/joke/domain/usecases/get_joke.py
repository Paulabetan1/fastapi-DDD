from abc import abstractmethod
from typing import Tuple

from app.core.error.joke_exception import JokeNotFoundError
from app.core.use_cases.use_case import BaseUseCase
from app.features.joke.domain.entities.joke_query_model import JokeReadModel
from app.features.joke.domain.services.joke_query_service import JokeQueryService


class GetjokeUseCase(BaseUseCase[Tuple[int], JokeReadModel]):

    service: JokeQueryService

    @abstractmethod
    def __call__(self, args: Tuple[int]) -> JokeReadModel:
        raise NotImplementedError()


class GetjokeUseCaseImpl(GetjokeUseCase):

    def __init__(self, service: JokeQueryService):
        self.service: JokeQueryService = service

    def __call__(self, args: Tuple[int]) -> JokeReadModel:
        id_, = args
        try:
            joke = self.service.find_by_id(id_)
            if joke is None:
                raise JokeNotFoundError()
        except Exception:
            raise

        return joke