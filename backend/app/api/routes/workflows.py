from uuid import uuid4

from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.workflow import Workflow
from app.orchestrator.runtime import WorkflowRuntime

router = APIRouter()


class WorkflowRequest(BaseModel):
    task: str


@router.post("/workflows")
def create_workflow(request: WorkflowRequest):

    db: Session = SessionLocal()

    try:

        workflow_id = uuid4()

        workflow = Workflow(
            id=workflow_id,
            name=request.task,
            status="running",
        )

        db.add(workflow)

        db.commit()

        db.refresh(workflow)

        initial_state = {
            "workflow_id": str(workflow_id),
            "status": "pending",
            "current_node": "planner",
            "input_data": {
                "task": request.task
            },
            "execution_plan": None,
            "execution_result": None,
            "review_status": None,
            "retry_count": 0,
        }

        runtime = WorkflowRuntime()

        result = runtime.execute(initial_state)

        workflow.status = "completed"

        db.commit()

        return {
            "workflow_id": str(workflow_id),
            "result": result,
        }

    except Exception as e:

        workflow.status = "failed"

        db.commit()

        return {
            "error": str(e)
        }

    finally:

        db.close()