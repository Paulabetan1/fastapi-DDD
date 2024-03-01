from fastapi import status, Depends, HTTPException, Response, Request

from app.features.joke.dependencies import get_create_joke_use_case
from app.features.joke.domain.entities.joke_command_model import JokeCreateModel
from app.features.joke.domain.entities.joke_query_model import JokeReadModel
from app.features.joke.domain.usecases.create_joke import CreatejokeUseCase
from app.features.joke.presentation.routes import router


@router.post(
    '/',
    response_model=JokeReadModel,
    status_code=status.HTTP_201_CREATED,
)
def create_joke(
    data: JokeCreateModel,
    response: Response,
    request: Request,
    create_joke_use_case: CreatejokeUseCase = Depends(get_create_joke_use_case)
):
    try:
        joke = create_joke_use_case((data, ))
    except Exception as _exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    response.headers['location'] = f"{request.url.path}{joke.id_}"
    return joke
