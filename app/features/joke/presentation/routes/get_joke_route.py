from fastapi import Depends, status, HTTPException

from app.core.error.joke_exception import JokeNotFoundError
from app.features.joke.dependencies import get_joke_use_case
from app.features.joke.domain.entities.joke_query_model import JokeReadModel
from app.features.joke.domain.usecases.get_joke import GetjokeUseCase
from app.features.joke.presentation.routes import router
from app.features.joke.presentation.schemas.joke_error_message import ErrorMessageJokeNotFound


@router.get(
    '/{id_}/',
    response_model=JokeReadModel,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorMessageJokeNotFound
        }
    }
)
def get_joke(
    id_: int,
    get_joke_use_case_: GetjokeUseCase = Depends(get_joke_use_case)
):
    try:
        joke = get_joke_use_case_((id_, ))
    except JokeNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return joke
