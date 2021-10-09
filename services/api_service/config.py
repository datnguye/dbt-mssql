from pydantic import BaseSettings
import os
from libs.yml_helper import load_yaml_text


with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/.ini.yml"
    ) as init_file:
    initial_info = load_yaml_text(init_file)
DEBUG = bool(initial_info.debug)

DBT_SINGLETON = initial_info.dbt.singleton
DBT_TARGET = initial_info.dbt.target
DBT_PROJECT_DIR = initial_info.dbt.project_dir


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Awesome dbt"

    def __get_storage__(type: str):
        """
        Get storage configuration dict
        """
        if type == "pickle":
            return dict(
                type=type,
                path=initial_info.log_storage[0].path
            )

        if type == "sqlserver":
            return dict(
                type=type,
                server=os.environ[initial_info.log_storage[0].server],
                port=initial_info.log_storage[0].port or 1433,
                database=initial_info.log_storage[0].database,
                user=os.environ[initial_info.log_storage[0].user],
                password=os.environ[initial_info.log_storage[0].password]
            )

        return None


    LOG_STORAGE = None
    if initial_info.log_storage and len(initial_info.log_storage) > 0:
        type = initial_info.log_storage[0].type
        LOG_STORAGE = __get_storage__(type=type)


settings = Settings()
