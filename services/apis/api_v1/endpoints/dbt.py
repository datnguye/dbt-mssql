from typing import Any
from fastapi import APIRouter
from schemas import token

router = APIRouter()

@router.post("/provision", response_model=token.Token)
def provision() -> Any:
    """
    Run dbt FULL for all models
    """
    pass


@router.post("/processing", response_model=token.Token)
def processing() -> Any:
    """
    Run dbt DELTA for all models
    """
    pass