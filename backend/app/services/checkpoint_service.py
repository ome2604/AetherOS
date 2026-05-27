from sqlalchemy.orm import Session

from app.models.workflow_checkpoint import (
    WorkflowCheckpoint,
)

from app.repositories.checkpoint_repository import (
    CheckpointRepository,
)


class CheckpointService:

    @staticmethod
    def save_checkpoint(
        db: Session,
        workflow_id: str,
        node_name: str,
        workflow_state: dict,
        status: str,
        retry_count: int = 0,
    ):

        checkpoint = WorkflowCheckpoint(
            workflow_id=workflow_id,

            node_name=node_name,

            workflow_state=workflow_state,

            status=status,

            retry_count=str(retry_count),
        )

        return CheckpointRepository.create(
            db,
            checkpoint,
        )

    @staticmethod
    def get_latest_checkpoint(
        db: Session,
        workflow_id: str,
    ):

        return (
            CheckpointRepository.get_latest(
                db,
                workflow_id,
            )
        )