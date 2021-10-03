from typing import Any
from storage.base import BaseStorage


class PickleStorage(BaseStorage):
    def __init__(self, storage_config: dict) -> None:
        super().__init__(storage_config=storage_config)
        self.path = storage_config["path"]


    def save(self, id: str, data: Any) -> bool:
        # TODO: Save to pickle file
        return True



    def get(self, id) -> Any:
        # TODO: get from to pickle file
        return None