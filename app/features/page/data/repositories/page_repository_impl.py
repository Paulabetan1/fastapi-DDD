from typing import Sequence

from sqlalchemy import select, update, delete
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from app.features.page.domain.entities.page_entity import PageEntity
from app.features.page.data.models.page import Page
from app.features.page.domain.repositories.page_repository import PageRepository


class PageRepositoryImpl(PageRepository):
    """
        PageRepositoryImpl implements CRUD operations related page entity using SQLAlchemy
    """

    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_email(self, email: str) -> PageEntity | None:
        statement = select(Page).filter_by(email=email)

        try:
            result: Page = self.session.execute(statement).scalar_one()
        except NoResultFound:
            return None

        return result.to_entity()

    def create(self, entity: PageEntity) -> PageEntity:
        page = Page.from_entity(entity)

        self.session.add(page)

        return page.to_entity()

    def findall(self) -> Sequence[PageEntity]:
        # TODO: add offset and limit
        statement = select(Page)

        try:
            result: Sequence[Page] = self.session.execute(statement).scalars().all()
        except NoResultFound:
            return []

        return [page.to_entity() for page in result]

    def find_by_id(self, id_: int) -> PageEntity | None:
        result: Page | None = self.session.get(Page, id_)

        if result is None:
            return None

        return result.to_entity()

    def update(self, entity: PageEntity) -> PageEntity:
        page = Page.from_entity(entity)
        update_data = page.to_dict()

        for key in [Page.updated_at.key, Page.created_at.key, Page.id_.key]:
            update_data.pop(key),

        statement = update(
            Page
        ).where(
            Page.id_ == page.id_
        ).values(
            update_data
        ).returning(
            Page
        )

        page_mapping = self.session.execute(statement).mappings().one()
        result = page(**page_mapping)

        return result.to_entity()

    def delete_by_id(self, id_: int) -> PageEntity:
        statement = delete(
            Page
        ).filter_by(
            id_=id_
        ).returning(
            *Page.__table__.columns
        )

        result: Page = self.session.execute(statement).scalar_one()

        return result.to_entity()
