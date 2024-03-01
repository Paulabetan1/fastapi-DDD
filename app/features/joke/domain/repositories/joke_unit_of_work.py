from app.core.unit_of_work.unit_of_work import AbstractUnitOfWork
from app.features.joke.domain.repositories.joke_repository import JokeRepository


class JokeUnitOfWork(AbstractUnitOfWork[JokeRepository]):
    pass
