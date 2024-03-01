from app.core.unit_of_work.unit_of_work import AbstractUnitOfWork
from app.features.page.domain.repositories.page_repository import PageRepository


class PageUnitOfWork(AbstractUnitOfWork[PageRepository]):
    """
    defines an interface based on Unit of Work
    """
    pass
