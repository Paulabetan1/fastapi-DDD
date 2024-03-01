from fastapi import Depends, HTTPException, status

from app.core.error.page_exception import PageNotFoundError
from app.features.page.dependencies import get_update_page_use_case
from app.features.page.domain.entities.page_command_model import PageUpdateModel
from app.features.page.domain.entities.page_query_model import PageReadModel
from app.features.page.domain.usecases.update_page import UpdatePageUseCase
from app.features.page.presentation.routes import router
from app.features.page.presentation.schemas.page_error_message import ErrorMessagePageNotFound


@router.patch(
    '/{id_}/',
    response_model=PageReadModel,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorMessagePageNotFound
        }
    }
)
async def update_page(
    id_: int,
    data: PageUpdateModel,
    update_page_use_case: UpdatePageUseCase = Depends(get_update_page_use_case)
):
    try:
        page = update_page_use_case((id_, data))
    except PageNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return page
