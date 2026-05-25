from sqlalchemy.orm import Session

from app.orchestrator.workflow import workflow_graph
from app.services.checkpoint_service import (
    CheckpointService
)


class WorkflowRuntime:

    @staticmethod
    def execute(
        db: Session,
        initial_state
    ):

        workflow_id = initial_state["workflow_id"]

        CheckpointService.create_checkpoint(
            db,
            workflow_id,
            "START",
            initial_state
        )

        result = workflow_graph.invoke(
            initial_state
        )

        CheckpointService.create_checkpoint(
            db,
            workflow_id,
            "END",
            result
        )

        return result