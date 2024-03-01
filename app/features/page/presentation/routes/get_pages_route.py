from fastapi import Depends, HTTPException, status

from app.features.page.dependencies import get_pages_use_case
from app.features.page.domain.entities.page_query_model import PageReadModel
from app.features.page.domain.usecases.get_pages import GetPagesUseCase
from app.features.page.presentation.routes import router
from app.features.page.presentation.schemas.page_error_message import ErrorMessagePagesNotFound


@router.get(
    '/',
    response_model=list[PageReadModel],
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorMessagePagesNotFound
        }
    }
)
def get_pages(skip: int = 0, limit: int = 100, get_pages_use_case_: GetPagesUseCase = Depends(get_pages_use_case)):
    try:
        pages = get_pages_use_case_(None)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    if not pages:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )

    return pages
