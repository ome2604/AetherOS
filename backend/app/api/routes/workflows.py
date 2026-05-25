from uuid import uuid4

from fastapi import APIRouter

from app.orchestrator.workflow import workflow_graph

router = APIRouter()


@router.post("/execute")
async def execute_workflow(payload: dict):

    workflow_id = str(uuid4())

    initial_state = {
        "workflow_id": workflow_id,
        "input": payload.get("input"),
        "output": None,
        "status": "pending",
    }

    result = workflow_graph.invoke(initial_state)

    return {
        "workflow_id": workflow_id,
        "status": result["status"],
        "output": result["output"],
    }