from fastapi import Depends, HTTPException, status

from app.core.error.joke_exception import JokeNotFoundError
from app.features.joke.dependencies import get_update_joke_use_case
from app.features.joke.domain.entities.joke_command_model import JokeUpdateModel
from app.features.joke.domain.entities.joke_query_model import JokeReadModel
from app.features.joke.domain.usecases.update_joke import UpdatejokeUseCase
from app.features.joke.presentation.routes import router
from app.features.joke.presentation.schemas.joke_error_message import ErrorMessageJokeNotFound


@router.put(
    '/{id_}/',
    response_model=JokeReadModel,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorMessageJokeNotFound
        }
    }
)
async def update_joke(
    id_: int,
    data: JokeUpdateModel,
    update_joke_use_case: UpdatejokeUseCase = Depends(get_update_joke_use_case)
):
    try:
        user = update_joke_use_case((id_, data))
    except JokeNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return user
