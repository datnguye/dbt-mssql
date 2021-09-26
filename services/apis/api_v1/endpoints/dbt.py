from typing import Any
from fastapi import APIRouter, BackgroundTasks
import schemas
from aha_dbt.dbt import instance

router = APIRouter()

def dbt_run(full: bool = True):
    """
    dbt_run
    """
    result = None
    if full:
        result = instance.run_full()
    else:        
        result = instance.run_delta()

    return result #TODO: Parse result to readable message


@router.post("/provision", response_model=schemas.Msg)
async def provision(
    background_tasks: BackgroundTasks
) -> Any:
    """
    Run dbt FULL for all models
    """
    background_tasks.add_task(dbt_run, full=True)
    return {"msg": "Provision job has been sent in the background"}


@router.post("/processing", response_model=schemas.Msg)
async def processing(
    background_tasks: BackgroundTasks
) -> Any:
    """
    Run dbt DELTA for all models
    """
    background_tasks.add_task(dbt_run, full=False)
    return {"msg": "Processing job has been sent in the background"}