from sqlalchemy.orm import Session

from AetherOS.backend.app.models.workflow_checkpoint import WorkflowCheckpoint


class ExecutionHistoryService:

    @staticmethod
    def get_workflow_history(
        db: Session,
        workflow_id,
    ):

        history = (
            db.query(WorkflowCheckpoint)
            .filter(
                WorkflowCheckpoint.workflow_id == workflow_id
            )
            .order_by(
                WorkflowCheckpoint.created_at.asc()
            )
            .all()
        )

        return history