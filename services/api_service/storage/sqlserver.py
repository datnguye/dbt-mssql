import os
import uuid
from typing import Any
from storage.base import BaseStorage
from sqlmodel import Session, Field, SQLModel, create_engine
from datetime import datetime


class DbtLog(SQLModel, table=True, table_name="__Dbt_Log"):
    Id: int = Field(default=None, primary_key=True)
    TaskId: str = Field(max_length=128)
    Data: str = Field(index=False)
    Timestamp: datetime = Field(index=False, default=datetime.utcnow())
    

class SqlServerStorage(BaseStorage):
    def __init__(self, storage_config: dict = None) -> None:
        super().__init__(storage_config=storage_config)
        self.url_template = "mssql+pyodbc://{user}:{password}@{server}:{port}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
        self.engine = create_engine(
            url=self.url_template.format(
                    user=self.storage_config['user'],
                    password=self.storage_config['password'],
                    server=self.storage_config['server'],
                    port=self.storage_config['port'],
                    database=self.storage_config['database']
                )
        )
        SQLModel.metadata.create_all(
            bind=self.engine
            #TODO Specify tables
        )
            
        

    
    # def __migration__(self):
    #     """
    #     Initial schema
    #     """
    #     migration_dir = f"{os.path.dirname(os.path.realpath(__file__))}/sqlserver_migrations"
    #     migration_sqls = [
    #         f for f in os.listdir(migration_dir) 
    #         if f.startswith("mig_") and f.endswith(".sql")
    #     ]

    #     # get the last migration
        

    #     # run migration from the last one
    #     for sql in migration_sqls.sort():
    #         pass


    def save(self, id: str, data: Any) -> bool:
        engine = create_engine(
            url=self.url_template.format(
                    user=self.storage_config['user'],
                    password=self.storage_config['password'],
                    server=self.storage_config['server'],
                    port=self.storage_config['port'],
                    database=self.storage_config['database']
                )
        )
        with Session(bind=engine) as session:
            session.add(DbtLog(TaskId=id, Data=str(data)))
            session.commit()

        return True

    
    def get(self, id) -> Any:
        return super().get(id)