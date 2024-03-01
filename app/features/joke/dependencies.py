from fastapi import Depends
from sqlalchemy.orm import Session

from app.features.joke.data.repositories.joke_repository_impl import JokeRepositoryImpl
from app.features.joke.data.repositories.joke_unit_of_work_impl import JokeUnitOfWorkImpl
from app.features.joke.data.services.joke_query_service_impl import JokeQueryServiceImpl
from app.features.joke.domain.repositories.joke_repository import JokeRepository
from app.features.joke.domain.repositories.joke_unit_of_work import JokeUnitOfWork
from app.features.joke.domain.services.joke_query_service import JokeQueryService
from app.features.joke.domain.usecases.create_joke import CreatejokeUseCase, CreatejokeUseCaseImpl
from app.features.joke.domain.usecases.delete_joke import DeletejokeUseCase, DeletejokeUseCaseImpl
from app.features.joke.domain.usecases.get_joke import GetjokeUseCase, GetjokeUseCaseImpl
from app.features.joke.domain.usecases.get_jokes import GetjokesUseCase, GetjokesUseCaseImpl
from app.features.joke.domain.usecases.update_joke import UpdatejokeUseCase, UpdatejokeUseCaseImpl
from app.core.database.postgres.database import get_session


def get_joke_query_service(
    session: Session = Depends(get_session)
) -> JokeQueryService:
    return JokeQueryServiceImpl(session)


def get_joke_repository(session: Session = Depends(get_session)) -> JokeRepository:
    return JokeRepositoryImpl(session)


def get_joke_unit_of_work(
    session: Session = Depends(get_session),
    joke_repository: JokeRepository = Depends(get_joke_repository)
) -> JokeUnitOfWork:
    return JokeUnitOfWorkImpl(session, joke_repository)


def get_jokes_use_case(
    joke_query_service: JokeQueryService = Depends(get_joke_query_service)
) -> GetjokesUseCase:
    return GetjokesUseCaseImpl(joke_query_service)


def get_create_joke_use_case(
    joke_unit_of_work: JokeUnitOfWork = Depends(get_joke_unit_of_work)
) -> CreatejokeUseCase:
    return CreatejokeUseCaseImpl(joke_unit_of_work)


def get_delete_joke_use_case(
    joke_unit_of_work: JokeUnitOfWork = Depends(get_joke_unit_of_work)
) -> DeletejokeUseCase:
    return DeletejokeUseCaseImpl(joke_unit_of_work)


def get_joke_use_case(
    joke_query_service: JokeQueryService = Depends(get_joke_query_service)
) -> GetjokeUseCase:
    return GetjokeUseCaseImpl(joke_query_service)


def get_update_joke_use_case(
    joke_unit_of_work: JokeUnitOfWork = Depends(get_joke_unit_of_work)
) -> UpdatejokeUseCase:
    return UpdatejokeUseCaseImpl(joke_unit_of_work)
