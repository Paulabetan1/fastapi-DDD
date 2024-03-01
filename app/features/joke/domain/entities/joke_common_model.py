from pydantic import Field, BaseModel


class JokeBaseModel(BaseModel):
    title: str = Field(example='Example todo title')
    owner_id: int = Field(example=1)
