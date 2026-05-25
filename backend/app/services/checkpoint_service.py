import json

from sqlalchemy.orm import Session

from app.models.checkpoint import WorkflowCheckpoint


class CheckpointService:

    @staticmethod
    def create_checkpoint(
        db: Session,
        workflow_id,
        node_name,
        state_data
    ):

        checkpoint = WorkflowCheckpoint(
            workflow_id=workflow_id,
            node_name=node_name,
            state_data=json.dumps(state_data)
        )

        db.add(checkpoint)

        db.commit()

        db.refresh(checkpoint)

        return checkpoint

    @staticmethod
    def get_latest_checkpoint(
        db: Session,
        workflow_id
    ):

        return (
            db.query(WorkflowCheckpoint)
            .filter(
                WorkflowCheckpoint.workflow_id == workflow_id
            )
            .order_by(
                WorkflowCheckpoint.created_at.desc()
            )
            .first()
        )