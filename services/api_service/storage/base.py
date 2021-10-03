from typing import Any


class BaseStorage():
    def __init__(self, storage_config: dict = None) -> None:
        self.storage_config = storage_config
        self.type = self.storage_config["type"] \
            if self.storage_config else None
        

    def save(self, id: str, data: Any):
        pass
    
    
    def get(self, id) -> Any:
        pass