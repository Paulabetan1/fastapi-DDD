from pydantic import BaseModel, Field


class PageBaseModel(BaseModel):
    """
        UserBase common fields
    """
    email: str = Field(example='test@test.com')
