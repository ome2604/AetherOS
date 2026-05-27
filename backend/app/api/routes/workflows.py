from uuid import uuid4

from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.session import SessionLocal

from app.models.workflow import Workflow

from app.workers.workflow_tasks import (
    execute_workflow,
)

router = APIRouter()


class WorkflowRequest(BaseModel):
    task: str


@router.post("/workflows")
def create_workflow(
    request: WorkflowRequest,
):

    db: Session = SessionLocal()

    try:

        workflow_id = uuid4()

        workflow = Workflow(
            id=workflow_id,

            name=request.task,

            status="pending",
        )

        db.add(workflow)

        db.commit()

        db.refresh(workflow)

        execute_workflow.delay(
            str(workflow_id),
            request.task,
        )

        return {
            "workflow_id": str(
                workflow_id
            ),

            "status": "queued",
        }

    except Exception as e:

        db.rollback()

        return {
            "error": str(e)
        }

    finally:

        db.close()


@router.get("/workflows")
def get_workflows():

    db: Session = SessionLocal()

    try:

        workflows = (
            db.query(Workflow)
            .all()
        )

        return [
            {
                "id": str(
                    workflow.id
                ),

                "name": workflow.name,

                "status": workflow.status,

                "created_at": workflow.created_at,
            }
            for workflow in workflows
        ]

    finally:

        db.close()