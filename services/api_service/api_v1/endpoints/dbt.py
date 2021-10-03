from typing import Any
from fastapi import APIRouter, BackgroundTasks
import schemas
from aha_dbt.dbt import instance, DBT, DbtAction
from config import DBT_PROJECT_DIR, DBT_TARGET

router = APIRouter()

def dbt_run(
    full: bool = True,
    *args,
    **kwargs
):
    """
    dbt_run
    """
    result = None
    if full:
        result = instance.execute("Provisioning flow", [
            DBT(
                action=DbtAction.SEED,
                target="failed",
                project_dir=DBT_PROJECT_DIR,
                full_refresh=True
            ),
            DBT(
                action=DbtAction.RUN,
                target=DBT_TARGET,
                project_dir=DBT_PROJECT_DIR,
                models='+exposure:*',
                full_refresh=True
            )
        ])
    else:        
        result = instance.execute("Processing flow", [
            DBT(
                action=DbtAction.RUN,
                target=DBT_TARGET,
                project_dir=DBT_PROJECT_DIR,
                models='+exposure:*'
            )
        ])

    # TODO: Custom run

    return result #TODO: Parse result to readable message


@router.post("/provision", response_model=schemas.TaskMsg)
async def provision(
    background_tasks: BackgroundTasks
) -> Any:
    """
    Run dbt FULL for all models
    """
    background_tasks.add_task(dbt_run, full=True)
    return dict(
        taskid="#TODO",
        msg="Provision job has been sent in the background"
    ) # TODO: Return task ID


@router.get("/provision/{taskid}", response_model=schemas.Msg)
async def get_provision_status(
    taskid: str
) -> Any:
    """
    get_provision_status
    """
    return {"msg": f"Status of task:{taskid} - Unknown"} # TODO: Get status of task


@router.post("/processing", response_model=schemas.TaskMsg)
async def processing(
    background_tasks: BackgroundTasks
) -> Any:
    """
    Run dbt DELTA for all models
    """
    background_tasks.add_task(dbt_run, full=False)
    return dict(
        taskid="#TODO",
        msg="Processing job has been sent in the background"
    ) # TODO: Return task ID


@router.get("/processing/{taskid}", response_model=schemas.Msg)
async def get_processing_status(
    taskid: str
) -> Any:
    """
    get_processing_status
    """
    return {"msg": f"Status of task:{taskid} - Unknown"} # TODO: Get status of task


@router.post("/custom-run", response_model=schemas.TaskMsg)
async def custom_run(
    background_tasks: BackgroundTasks,
    *args,
    **kwargs
) -> Any:
    """
    Run dbt in whatever its native arguments
    """
    background_tasks.add_task(dbt_run, args, kwargs)
    return dict(
        taskid="#TODO",
        msg="A dbt job has been sent in the background"
    ) # TODO: Return task ID


@router.get("/custom-run/{taskid}", response_model=schemas.Msg)
async def get_custom_run_status(
    taskid: str
) -> Any:
    """
    get_custom_run_status
    """
    return {"msg": f"Status of task:{taskid} - Unknown"} # TODO: Get status of task