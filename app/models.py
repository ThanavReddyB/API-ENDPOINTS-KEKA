from pydantic import BaseModel


class SampleRequest(BaseModel):
    name: str
    value: int


class SampleResponse(BaseModel):
    id: int
    name: str
    value: int
    message: str
