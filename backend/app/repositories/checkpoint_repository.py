from sqlalchemy.orm import Session

from app.models.workflow_checkpoint import (
    WorkflowCheckpoint,
)


class CheckpointRepository:

    @staticmethod
    def create(
        db: Session,
        checkpoint: WorkflowCheckpoint,
    ):

        db.add(checkpoint)

        db.commit()

        db.refresh(checkpoint)

        return checkpoint

    @staticmethod
    def get_latest(
        db: Session,
        workflow_id: str,
    ):

        return (
            db.query(WorkflowCheckpoint)
            .filter(
                WorkflowCheckpoint.workflow_id
                == workflow_id
            )
            .order_by(
                WorkflowCheckpoint.created_at.desc()
            )
            .first()
        )

    @staticmethod
    def list_by_workflow(
        db: Session,
        workflow_id: str,
    ):

        return (
            db.query(WorkflowCheckpoint)
            .filter(
                WorkflowCheckpoint.workflow_id
                == workflow_id
            )
            .all()
        )