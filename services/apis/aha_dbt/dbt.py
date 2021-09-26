from pydantic import BaseModel
from prefect import Flow
from prefect.tasks.dbt import DbtShellTask

class DBT(BaseModel):

    def run_full(self):
        """
        Run dbt FULL
        """
        with Flow(name="dbt-run-full") as f:
            DbtShellTask(
                profile_name='dbt_mssql',
                environment="dev",
                set_profiles_envar=False,
                return_all=True,
                log_stderr=True
            )(command='dbt run --full-refresh')

        return f.run()


    def run_delta(self):
        """
        Run dbt DELTa
        """
        with Flow(name="dbt-run-delta") as f:
            DbtShellTask(
                profile_name='dbt_mssql',
                environment="dev",
                set_profiles_envar=False,
                return_all=True,
                log_stderr=True
            )(command='dbt run')

        return f.run()

instance = DBT()