from sqlalchemy.orm import Session

from app.services.checkpoint_service import (
    CheckpointService,
)


class SnapshotManager:

    @staticmethod
    def persist_snapshot(
        db: Session,
        workflow_id: str,
        node_name: str,
        state: dict,
        status: str,
    ):

        return (
            CheckpointService.save_checkpoint(
                db=db,

                workflow_id=workflow_id,

                node_name=node_name,

                workflow_state=state,

                status=status,
            )
        )