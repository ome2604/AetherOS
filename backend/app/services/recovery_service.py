from sqlalchemy.orm import Session

from app.models.checkpoint import WorkflowCheckpoint


class RecoveryService:

    @staticmethod
    def get_latest_checkpoint(
        db: Session,
        workflow_id,
    ):

        checkpoint = (
            db.query(WorkflowCheckpoint)
            .filter(
                WorkflowCheckpoint.workflow_id == workflow_id
            )
            .order_by(
                WorkflowCheckpoint.created_at.desc()
            )
            .first()
        )

        return checkpoint