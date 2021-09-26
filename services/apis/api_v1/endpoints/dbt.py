from typing import Any
from fastapi import APIRouter, BackgroundTasks
import schemas

router = APIRouter()

def dbt_run(mode: str = "FULL"):
    """
    dbt_run
    """
    print(f"dbt_run as {mode}")


@router.post("/provision", response_model=schemas.Msg)
async def provision(
    background_tasks: BackgroundTasks
) -> Any:
    """
    Run dbt FULL for all models
    """
    background_tasks.add_task(dbt_run, mode="FULL")
    return {"msg": "Provision job has been sent in the background"}


@router.post("/processing", response_model=schemas.Msg)
async def processing(
    background_tasks: BackgroundTasks
) -> Any:
    """
    Run dbt DELTA for all models
    """
    background_tasks.add_task(dbt_run, mode="DELTA")
    return {"msg": "Processing job has been sent in the background"}