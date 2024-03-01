from abc import abstractmethod
from typing import Sequence

from app.core.use_cases.use_case import BaseUseCase
from app.features.joke.domain.entities.joke_query_model import JokeReadModel
from app.features.joke.domain.services.joke_query_service import JokeQueryService


class GetjokesUseCase(BaseUseCase[None, Sequence[JokeReadModel]]):

    service: JokeQueryService

    @abstractmethod
    def __call__(self, args: None) -> Sequence[JokeReadModel]:
        raise NotImplementedError()


class GetjokesUseCaseImpl(GetjokesUseCase):

    def __init__(self, service: JokeQueryService):
        self.service: JokeQueryService = service

    def __call__(self, args: None) -> Sequence[JokeReadModel]:
        try:
            jokes = self.service.findall()
        except Exception:
            raise

        return jokes