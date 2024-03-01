from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.features.joke.data.models.joke import Joke
from app.features.joke.domain.entities.joke_query_model import JokeReadModel
from app.features.joke.domain.services.joke_query_service import JokeQueryService


class JokeQueryServiceImpl(JokeQueryService):

    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_id(self, id_: int) -> JokeReadModel | None:
        result = self.session.get(Joke, id_)

        if result is None:
            return None

        return result.to_read_model()

    def findall(self) -> Sequence[JokeReadModel]:
        # TODO: add offset and limit
        statement = select(Joke)

        result = self.session.execute(statement).scalars().all()

        if len(result) == 0:
            return []

        return [Joke.to_read_model() for Joke in result]
