
from fastapi import Depends, HTTPException, status

from app.core.error.page_exception import PageNotFoundError
from app.features.page.dependencies import get_page_use_case
from app.features.page.domain.entities.page_query_model import PageReadModel
from app.features.page.domain.usecases.get_page import GetPageUseCase
from app.features.page.presentation.routes import router
from app.features.page.presentation.schemas.page_error_message import ErrorMessagePageNotFound


@router.get(
    '/{id_}/',
    response_model=PageReadModel,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorMessagePageNotFound
        }
    }
)
def get_page(
    id_: int,
    get_page_use_case_: GetPageUseCase = Depends(get_page_use_case)
):
    try:
        page = get_page_use_case_((id_, ))
    except PageNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return page
