"""
    page Api Router
"""
from fastapi import Depends, HTTPException, status

from app.core.error.page_exception import PageNotFoundError
from app.features.page.dependencies import get_delete_page_use_case
from app.features.page.domain.entities.page_query_model import PageReadModel
from app.features.page.domain.usecases.delete_page import DeletePageUseCase
from app.features.page.presentation.routes import router
from app.features.page.presentation.schemas.page_error_message import ErrorMessagePageNotFound


@router.delete(
    '/{id_}/',
    response_model=PageReadModel,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorMessagePageNotFound
        }
    }
)
def delete_page(
    id_: int,
    delete_page_use_case: DeletePageUseCase = Depends(get_delete_page_use_case)
):
    try:
        page = delete_page_use_case((id_, ))
    except PageNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return page
