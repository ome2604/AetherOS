from sqlalchemy.orm import Session

from app.runtime.snapshot_manager import (
    SnapshotManager,
)


class GraphCheckpointManager:

    @staticmethod
    def save_checkpoint(
        db: Session,
        workflow_id: str,
        node_name: str,
        state: dict,
    ):

        SnapshotManager.persist_snapshot(

            db=db,

            workflow_id=workflow_id,

            node_name=node_name,

            state=state,

            status=state.get(
                "status",
                "running",
            ),
        )