from pydantic import BaseModel
from prefect import Flow, Task

class DBT(BaseModel):

    def run(self):
        print("DBT run")
        pass

    def run_full(self):
        """
        Run dbt FULL
        """
        with Flow(name="dbt_run_full") as f:
            self.run()

        return f.run()

instance = DBT()