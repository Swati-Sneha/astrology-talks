from datetime import datetime
from typing import Any, Generic, Mapping, TypeVar, Union

from motor.motor_asyncio import AsyncIOMotorCollection

from app.database.db import Database

ModelType = TypeVar("ModelType")
DocumentType = TypeVar("DocumentType", bound=Mapping[str, Any])


class BaseCrud(Generic[ModelType]):

    _model_class: Union[ModelType, None] = None
    _collection_name: Union[str, None] = None

    def __init__(self) -> None:
        """Init the BaseCrud instance and set the collection document link to the model."""
        if not (self._model_class and self._collection_name):
            raise RuntimeError(
                "Model or collection name is missing initialising DB interface."
            )

        self._model = self._model_class

    @property
    def _collection(self) -> AsyncIOMotorCollection:
        return Database().db[self._collection_name] # type: ignore
