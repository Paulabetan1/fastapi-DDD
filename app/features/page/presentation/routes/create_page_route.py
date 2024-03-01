from fastapi import Depends, HTTPException, status, Response, Request

from app.core.error.page_exception import PageAlreadyExistsError
from app.features.page.dependencies import get_create_page_use_case
from app.features.page.domain.entities.page_command_model import PageCreateModel
from app.features.page.domain.entities.page_query_model import PageReadModel
from app.features.page.domain.usecases.create_page import CreatePageUseCase
from app.features.page.presentation.routes import router
from app.features.page.presentation.schemas.page_error_message import ErrorMessagePageAlreadyExists


@router.post(
    '/',
    response_model=PageReadModel,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_409_CONFLICT: {
            'model': ErrorMessagePageAlreadyExists
        }
    },
)
def create_page(
    data: PageCreateModel,
    response: Response,
    request: Request,
    create_page_use_case: CreatePageUseCase = Depends(get_create_page_use_case),
):
    try:
        page = create_page_use_case((data, ))
    except PageAlreadyExistsError as exception:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=exception.message
        )
    except Exception as _exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    response.headers['location'] = f"{request.url.path}{page.id_}"
    return page
