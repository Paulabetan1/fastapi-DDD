from sqlalchemy.orm import Session

from app.features.page.domain.repositories.page_repository import PageRepository
from app.features.page.domain.repositories.page_unit_of_work import PageUnitOfWork


class PageUnitOfWorkImpl(PageUnitOfWork):
    """

    """

    def __init__(self, session: Session, page_repository: PageRepository):
        self.session: Session = session
        self.repository: PageRepository = page_repository

    def begin(self):
        self.session.begin()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
