from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.features.page.data.models.page import Page
from app.features.page.domain.entities.page_query_model import PageReadModel
from app.features.page.domain.services.page_query_service import PageQueryService


class PageQueryServiceImpl(PageQueryService):
    """
        PageQueryServiceImpl implements READ operations related to page entity using SQLALCHEMY
    """

    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_id(self, id_: int) -> PageReadModel | None:
        result = self.session.get(Page, id_)

        if result is None:
            return None

        return result.to_read_model()

    def findall(self) -> Sequence[PageReadModel]:
        # TODO: add offset and limit
        statement = select(Page).filter_by(is_deleted=False)

        result = self.session.execute(statement).scalars().all()

        return [page.to_read_model() for page in result]
