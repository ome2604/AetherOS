from uuid import uuid4

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.orchestrator.runtime import WorkflowRuntime

router = APIRouter()


@router.post("/execute")
async def execute_workflow(
    payload: dict,
    db: Session = Depends(get_db)
):

    workflow_id = str(uuid4())

    initial_state = {
        "workflow_id": workflow_id,
        "input": payload.get("input"),
        "output": None,
        "status": "pending",
    }

    result = WorkflowRuntime.execute(
        db,
        initial_state
    )

    return {
        "workflow_id": workflow_id,
        "status": result["status"],
        "output": result["output"],
    }