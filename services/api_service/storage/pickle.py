from typing import Any
from storage.base import BaseStorage


class PickleStorage(BaseStorage):
    def __init__(self, storage_config: dict = None) -> None:
        super().__init__(storage_config=storage_config)


    def save(self, id: str, data: Any):
        return super().save(id, data)


    def get(self, id) -> Any:
        return super().get(id)