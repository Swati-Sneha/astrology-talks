from typing import Any


class SingletonMeta(type):
    """The Singleton class implemented by using the meta-class."""

    _instances: dict["SingletonMeta", Any] = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
