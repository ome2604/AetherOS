from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.schemas.workflow import (
    WorkflowCreate,
    WorkflowResponse
)
from app.services.workflow_service import WorkflowService
from app.tasks.workflow_tasks import execute_workflow

router = APIRouter()


@router.post(
    "/workflows",
    response_model=WorkflowResponse
)
async def create_workflow(
    workflow: WorkflowCreate,
    db: Session = Depends(get_db)
):

    new_workflow = WorkflowService.create_workflow(
        db,
        workflow.name
    )

    execute_workflow.delay(
        str(new_workflow.id)
    )

    return new_workflow


@router.get(
    "/workflows",
    response_model=list[WorkflowResponse]
)
async def list_workflows(
    db: Session = Depends(get_db)
):

    return WorkflowService.list_workflows(db)


@router.get(
    "/workflows/{workflow_id}",
    response_model=WorkflowResponse
)
async def get_workflow(
    workflow_id: str,
    db: Session = Depends(get_db)
):

    return WorkflowService.get_workflow(
        db,
        workflow_id
    )