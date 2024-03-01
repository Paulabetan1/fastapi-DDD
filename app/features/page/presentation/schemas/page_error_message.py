from pydantic import BaseModel, Field

from app.core.error.page_exception import (
    PageNotFoundError,
    PagesNotFoundError,
    PageAlreadyExistsError
)


class ErrorMessagePageNotFound(BaseModel):
    detail: str = Field(example=PageNotFoundError.message)


class ErrorMessagePagesNotFound(BaseModel):
    detail: str = Field(example=PagesNotFoundError.message)


class ErrorMessagePageAlreadyExists(BaseModel):
    detail: str = Field(example=PageAlreadyExistsError.message)
