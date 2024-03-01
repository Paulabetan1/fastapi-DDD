from abc import abstractmethod
from typing import Sequence

from app.core.repositories.base_repository import BaseRepository
from app.features.joke.domain.entities.joke_entity import JokeEntity


class JokeRepository(BaseRepository[JokeEntity]):

    @abstractmethod
    def find_by_owner_id(self, owner_id: int) -> Sequence[JokeEntity]:
        raise NotImplementedError()