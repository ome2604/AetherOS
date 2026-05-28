from sqlalchemy.orm import Session

from app.models.workflow import (
    Workflow,
)


class WorkflowRepository:

    @staticmethod
    def get_workflow(
        db: Session,
        workflow_id: str,
    ):

        workflow = (

            db.query(
                Workflow
            )

            .filter(
                Workflow.id == workflow_id
            )

            .first()
        )

        return workflow