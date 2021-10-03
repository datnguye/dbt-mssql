from storage.base import BaseStorage
from storage.pickle import PickleStorage


class StorageFactory(object):
    def __init__(self, base: BaseStorage) -> None:
        super().__init__()
        self.base = base

    
    def get_storage_instance(self):
        if self.base.type is None:
            return self.base

        if self.base.type == "pickle":
            return PickleStorage(self.base.storage_config)