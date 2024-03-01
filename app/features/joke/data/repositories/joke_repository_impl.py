from typing import Sequence

from sqlalchemy import select, update, delete
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from app.features.joke.data.models.joke import Joke
from app.features.joke.domain.entities.joke_entity import JokeEntity
from app.features.joke.domain.repositories.joke_repository import JokeRepository


class JokeRepositoryImpl(JokeRepository):

    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_owner_id(self, owner_id: int) -> Sequence[JokeEntity]:
        statement = select(Joke).filter_by(owner_id=owner_id).order_by(Joke.created_at.desc())

        try:
            result: Sequence[Joke] = self.session.execute(statement).scalars().all()
        except NoResultFound:
            return []

        return [Joke.to_entity() for Joke in result]

    def create(self, entity: JokeEntity) -> JokeEntity:
        Joke = Joke.from_entity(entity)

        self.session.add(Joke)

        return Joke.to_entity()

    def findall(self) -> Sequence[JokeEntity]:
        # TODO: add offset and limit
        statement = select(Joke)

        try:
            result: Sequence[Joke] = self.session.execute(statement).scalars().all()
        except NoResultFound:
            return []

        return [Joke.to_entity() for Joke in result]

    def find_by_id(self, id_: int) -> JokeEntity | None:
        result: Joke | None = self.session.get(Joke, id_)

        if result is None:
            return None

        return result.to_entity()

    def update(self, entity: JokeEntity) -> JokeEntity:
        Joke = Joke.from_entity(entity)
        update_data = Joke.to_dict()

        for key in [Joke.updated_at.key, Joke.created_at.key, Joke.updated_at.key]:
            update_data.pop(key)

        statement = update(
            Joke
        ).filter_by(
            id_=Joke.id_
        ).values(
            update_data
        ).returning(
            Joke
        )

        Joke_mapping = self.session.execute(statement).mappings().one()
        result = Joke(**Joke_mapping)

        return Joke.to_entity()

    def delete_by_id(self, id_: int) -> JokeEntity:
        statement = delete(
            Joke
        ).filter_by(
            id_=id_
        ).returning(
            *Joke.__table__.columns
        )

        result: Joke = self.session.execute(statement).scalar_one()

        return result.to_entity()
