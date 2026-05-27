from sqlalchemy.orm import Session

from app.repositories.checkpoint_repository import (
    CheckpointRepository,
)


class GraphReplayEngine:

    @staticmethod
    def get_workflow_history(
        db: Session,
        workflow_id: str,
    ):

        checkpoints = (
            CheckpointRepository
            .list_by_workflow(
                db,
                workflow_id,
            )
        )

        history = []

        for checkpoint in checkpoints:

            history.append({

                "node_name":
                    checkpoint.node_name,

                "status":
                    checkpoint.status,

                "timestamp":
                    str(checkpoint.created_at),
            })

        return history