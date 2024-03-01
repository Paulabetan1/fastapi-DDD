from fastapi import Depends, status, HTTPException

from app.features.joke.presentation.routes import router
from app.features.joke.dependencies import get_jokes_use_case
from app.features.joke.domain.entities.joke_query_model import JokeReadModel
from app.features.joke.domain.usecases.get_jokes import GetjokesUseCase
from app.features.joke.presentation.schemas.joke_error_message import ErrorMessageJokesNotFound


@router.get(
    '/',
    response_model=list[JokeReadModel],
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorMessageJokesNotFound
        }
    }
)
def get_jokes(
    skip: int = 0,
    limit: int = 100,
    get_jokes_use_case_: GetjokesUseCase = Depends(get_jokes_use_case)
):
    try:
        jokes = get_jokes_use_case_(None)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    if not jokes:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )

    return jokes
