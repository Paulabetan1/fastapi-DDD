from sqlalchemy.orm import Session

from app.features.joke.domain.repositories.joke_repository import JokeRepository
from app.features.joke.domain.repositories.joke_unit_of_work import JokeUnitOfWork


class JokeUnitOfWorkImpl(JokeUnitOfWork):

    def __init__(self, session: Session, repository: JokeRepository):
        self.session: Session = session
        self.repository: JokeRepository = repository

    def begin(self):
        self.session.begin()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
