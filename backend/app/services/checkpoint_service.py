from uuid import UUID

from sqlalchemy.orm import Session

from app.models.checkpoint import WorkflowCheckpoint
from app.orchestrator.state import WorkflowState


def serialize_state(data):

    if isinstance(data, UUID):

        return str(data)

    if isinstance(data, dict):

        return {
            key: serialize_state(value)
            for key, value in data.items()
        }

    if isinstance(data, list):

        return [
            serialize_state(item)
            for item in data
        ]

    return data


class CheckpointService:

    @staticmethod
    def save_checkpoint(
        db: Session,
        state: WorkflowState,
    ):

        serialized_state = serialize_state(state)

        checkpoint = WorkflowCheckpoint(
            workflow_id=state["workflow_id"],
            node_name=state["current_node"],
            state=serialized_state,
        )

        db.add(checkpoint)

        db.commit()

        db.refresh(checkpoint)

        return checkpoint