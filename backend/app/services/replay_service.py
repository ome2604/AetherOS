from sqlalchemy.orm import Session

from app.repositories.replay_repository import (
    ReplayRepository,
)

from app.schemas.replay_schema import (
    WorkflowReplay,
)

from app.schemas.replay_schema import (
    ReplayStep,
)


class ReplayService:

    @staticmethod
    def generate_workflow_replay(
        db: Session,
        workflow_id: str,
    ):

        history = (

            ReplayRepository
            .get_workflow_history(
                db,
                workflow_id,
            )
        )

        timeline = []

        for checkpoint in history:

            step = ReplayStep(

                node_name=checkpoint.node_name,

                status=checkpoint.status,

                workflow_state=(
                    checkpoint.workflow_state
                ),

                created_at=str(
                    checkpoint.created_at
                ),
            )

            timeline.append(step)

        replay = WorkflowReplay(

            workflow_id=workflow_id,

            timeline=timeline,
        )

        return replay