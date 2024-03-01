from fastapi import HTTPException, Depends, status

from app.core.error.joke_exception import JokeNotFoundError
from app.features.joke.dependencies import get_delete_joke_use_case
from app.features.joke.domain.entities.joke_query_model import JokeReadModel
from app.features.joke.domain.usecases.delete_joke import DeletejokeUseCase
from app.features.joke.presentation.routes import router
from app.features.joke.presentation.schemas.joke_error_message import ErrorMessageJokeNotFound


@router.delete(
    '/{id_}/',
    response_model=JokeReadModel,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorMessageJokeNotFound
        }
    }
)
def delete_joke(
    id_: int,
    delete_joke_use_case: DeletejokeUseCase = Depends(get_delete_joke_use_case)
):
    try:
        joke = delete_joke_use_case((id_, ))
    except JokeNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return joke
