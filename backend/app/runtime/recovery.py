from sqlalchemy.orm import Session

from app.services.checkpoint_service import (
    CheckpointService,
)


class RecoveryManager:

    @staticmethod
    def recover_workflow(
        db: Session,
        workflow_id: str,
    ):

        checkpoint = (
            CheckpointService
            .get_latest_checkpoint(
                db,
                workflow_id,
            )
        )

        if not checkpoint:
            return None

        return {
            "node_name": checkpoint.node_name,

            "workflow_state":
                checkpoint.workflow_state,

            "status": checkpoint.status,
        }