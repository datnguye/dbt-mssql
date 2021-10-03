from typing import Any
from fastapi import APIRouter, BackgroundTasks
import schemas
from aha_dbt.dbt import instance, DBT, DbtAction
from config import DBT_PROJECT_DIR, DBT_TARGET
import libs

router = APIRouter()
PROJECT_DIR_ARGUMENT = "--project-dir"

def dbt_custom_run(arguments: list = []):
    """
    dbt custom run
    """
    taskid = arguments[0]

    dbt = DBT(
        action=arguments[1],
        args=arguments[2:]
    )
    if PROJECT_DIR_ARGUMENT not in arguments:
        dbt.project_dir=DBT_PROJECT_DIR
    result = instance.execute(f"Custom dbt flow | Task: {taskid}", [dbt])
    
    return result #TODO: Parse result to readable message


def dbt_run(taskid: str, full: bool = None):
    """
    dbt run
    """
    result = None
    if full: # Provision job
        result = instance.execute(f"Provisioning flow | Task: {taskid}", [
            DBT(
                action=DbtAction.SEED.value,
                target=DBT_TARGET,
                project_dir=DBT_PROJECT_DIR,
                full_refresh=True
            ),
            DBT(
                action=DbtAction.RUN.value,
                target=DBT_TARGET,
                project_dir=DBT_PROJECT_DIR,
                models='+exposure:*',
                full_refresh=True
            )
        ])
    else: # Processing job
        result = instance.execute(f"Processing flow | Task: {taskid}", [
            DBT(
                action=DbtAction.RUN.value,
                target=DBT_TARGET,
                project_dir=DBT_PROJECT_DIR,
                models='+exposure:*'
            )
        ])

    return result #TODO: Parse result to readable message


@router.post("/provision", response_model=schemas.TaskMsg)
async def provision(
    background_tasks: BackgroundTasks
) -> Any:
    """
    Run dbt FULL for all models
    """
    taskid = libs.new_taskid()
    background_tasks.add_task(dbt_run, taskid=taskid, full=True)
    return dict(
        taskid=taskid,
        msg="Provision job has been sent in the background"
    )


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
    taskid = libs.new_taskid()
    background_tasks.add_task(dbt_run, taskid=taskid, full=False)
    return dict(
        taskid=taskid,
        msg="Processing job has been sent in the background"
    )


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
    dbt_args: schemas.DbtArgument,
    background_tasks: BackgroundTasks
) -> Any:
    """
    Run dbt in whatever its native arguments
    """
    taskid = libs.new_taskid()
    args = [
        taskid,
        dbt_args.action
    ]
    
    args.extend(
        [x.value for x in dbt_args.args] \
        if dbt_args.args and len(dbt_args.args) > 0
        else []
    )
    
    if dbt_args.kwargs and len(dbt_args.kwargs) > 0:
        for kw in dbt_args.kwargs:
            args.extend([kw.key, kw.value])

    background_tasks.add_task(dbt_custom_run, arguments=args)
    return dict(
        taskid=taskid,
        msg="A dbt job has been sent in the background"
    )


@router.get("/custom-run/{taskid}", response_model=schemas.Msg)
async def get_custom_run_status(
    taskid: str
) -> Any:
    """
    get_custom_run_status
    """
    return {"msg": f"Status of task:{taskid} - Unknown"} # TODO: Get status of task