from pydantic import Field, BaseModel

from app.features.page.domain.entities.page_common_model import PageBaseModel


class PageCreateModel(PageBaseModel):
    """
        pageCreateModel represents a write model to create a page
    """
    password: str = Field(example='password')


class PageUpdateModel(BaseModel):
    """
        pageUpdateModel represents a write model to update a page
    """

    email: str | None
    password: str | None = Field(example='password')
    is_active: bool | None = Field(example=True)
    is_deleted: bool | None = Field(example=True)
