from sqlalchemy.orm import Session

from app.models.workflow_checkpoint import (
    WorkflowCheckpoint,
)


class ReplayRepository:

    @staticmethod
    def get_workflow_history(
        db: Session,
        workflow_id: str,
    ):

        checkpoints = (

            db.query(
                WorkflowCheckpoint
            )

            .filter(
                WorkflowCheckpoint.workflow_id
                == workflow_id
            )

            .order_by(
                WorkflowCheckpoint.created_at.asc()
            )

            .all()
        )

        return checkpoints