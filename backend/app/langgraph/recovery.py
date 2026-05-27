from sqlalchemy.orm import Session

from app.services.checkpoint_service import (
    CheckpointService,
)


class GraphRecoveryEngine:

    @staticmethod
    def recover_checkpoint(
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

            "node_name":
                checkpoint.node_name,

            "workflow_state":
                checkpoint.workflow_state,

            "status":
                checkpoint.status,
        }