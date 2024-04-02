from pydantic import BaseModel
from typing import Optional


class ErrorResponse(BaseModel):
    data: list = []
    message: str
    meta: dict = {"error": True}


class SuccessResponse(BaseModel):
    data: dict = {}
    message: str = ""
    meta: Optional[dict] = {"error": False}
