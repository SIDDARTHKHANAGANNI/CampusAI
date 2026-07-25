from typing import Generic, TypeVar

from pydantic import BaseModel
from pydantic.generics import GenericModel

T = TypeVar("T")


class SuccessResponse(BaseModel):
    success: bool = True
    message: str


class DataResponse(GenericModel, Generic[T]):
    success: bool = True
    message: str
    data: T