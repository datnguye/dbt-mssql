from typing import Any
from sqlalchemy.sql.expression import desc
from storage.sqlserver_schema import DbtLog
from storage.base import BaseStorage
from sqlmodel import Session, SQLModel, create_engine, select
from prefect.engine.state import Pending, Running, State, Success, TriggerFailed


class SqlServerStorage(BaseStorage):
    def __init__(self, storage_config: dict = None) -> None:
        super().__init__(storage_config=storage_config)
        self.engine = create_engine(
            url="mssql+pyodbc://{user}:{password}@{server}:{port}/{database}?driver=ODBC+Driver+17+for+SQL+Server"\
                .format(
                    user=self.storage_config['user'],
                    password=self.storage_config['password'],
                    server=self.storage_config['server'],
                    port=self.storage_config['port'],
                    database=self.storage_config['database']
                ),
            echo=True
        )
        SQLModel.metadata.create_all(
            bind=self.engine
        )
            
    
    def __migration__(self):
        """
        Schema mirgration
        """
        # migration_dir = f"{os.path.dirname(os.path.realpath(__file__))}/sqlserver_migrations"
        # migration_sqls = [
        #     f for f in os.listdir(migration_dir) 
        #     if f.startswith("mig_") and f.endswith(".sql")
        # ]

        # # get the last migration
        

        # # run migration from the last one
        # for sql in migration_sqls.sort():
        raise "Not yet impletmented"


    def save(self, id: str, data: Any) -> bool:
        with Session(bind=self.engine) as session:
            session.add(DbtLog(TaskId=id, Data=str(data)))
            session.commit()

        return True

    
    def get(self, id) -> State:
        with Session(bind=self.engine) as session:
            statement = select(DbtLog)\
                        .where(DbtLog.TaskId == id)\
                        .order_by(desc(DbtLog.Timestamp))\
                        .limit(1)
            result = session.exec(statement).first()

            if not result:
                return TriggerFailed(message=f"ID: {id} Not found")

            if "success" in result.Data.lower():
                return Success(message=result.Data)
            if "running" in result.Data.lower():
                return Running(message=result.Data)
            
            return Pending(message=result.Data)

