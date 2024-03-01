from fastapi import Depends
from sqlalchemy.orm import Session

from app.features.page.data.repositories.page_repository_impl import PageRepositoryImpl
from app.features.page.data.repositories.page_unit_of_work_impl import PageUnitOfWorkImpl
from app.features.page.data.services.page_query_service_impl import PageQueryServiceImpl
from app.features.page.domain.repositories.page_repository import PageRepository
from app.features.page.domain.repositories.page_unit_of_work import PageUnitOfWork
from app.features.page.domain.services.page_query_service import PageQueryService
from app.features.page.domain.usecases.create_page import CreatePageUseCase, CreatePageUseCaseImpl
from app.features.page.domain.usecases.delete_page import DeletePageUseCase, DeletePageUseCaseImpl
from app.features.page.domain.usecases.get_page import GetPageUseCase, GetPageUseCaseImpl
from app.features.page.domain.usecases.get_pages import GetPagesUseCaseImpl, GetPagesUseCase
from app.features.page.domain.usecases.update_page import UpdatePageUseCase, UpdatePageUseCaseImpl
from app.core.database.postgres.database import get_session


def get_page_query_service(session: Session = Depends(get_session)) -> PageQueryService:
    return PageQueryServiceImpl(session)


def get_page_repository(session: Session = Depends(get_session)) -> PageRepository:
    return PageRepositoryImpl(session)


def get_page_unit_of_work(
    session: Session = Depends(get_session),
    page_repository: PageRepository = Depends(get_page_repository),
) -> PageUnitOfWork:
    return PageUnitOfWorkImpl(session, page_repository)


def get_delete_page_use_case(
    unit_of_work: PageUnitOfWork = Depends(get_page_unit_of_work)
) -> DeletePageUseCase:
    return DeletePageUseCaseImpl(unit_of_work)


def get_page_use_case(
    page_query_service: PageQueryService = Depends(get_page_query_service)
) -> GetPageUseCase:
    """
        DI for page query use case
    """
    return GetPageUseCaseImpl(page_query_service)


def get_pages_use_case(
    page_query_service: PageQueryService = Depends(get_page_query_service)
) -> GetPagesUseCase:
    return GetPagesUseCaseImpl(page_query_service)


def get_create_page_use_case(
    unit_of_work: PageUnitOfWork = Depends(get_page_unit_of_work)
) -> CreatePageUseCase:
    return CreatePageUseCaseImpl(unit_of_work)


def get_update_page_use_case(
    unit_of_work: PageUnitOfWork = Depends(get_page_unit_of_work)
) -> UpdatePageUseCase:
    return UpdatePageUseCaseImpl(unit_of_work)
