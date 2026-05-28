from sqlalchemy.orm import Session

from app.models.workflow import (
    Workflow,
)

from app.repositories.workflow_repository import (
    WorkflowRepository,
)


class InterruptService:

    @staticmethod
    def pause_workflow(
        db: Session,
        workflow_id: str,
        reason: str,
    ):

        workflow = (
            WorkflowRepository
            .get_workflow(
                db,
                workflow_id,
            )
        )

        workflow.status = "paused"

        workflow.interrupt_reason = (
            reason
        )

        db.commit()

        db.refresh(workflow)

        return workflow

    @staticmethod
    def resume_workflow(
        db: Session,
        workflow_id: str,
    ):

        workflow = (
            WorkflowRepository
            .get_workflow(
                db,
                workflow_id,
            )
        )

        workflow.status = "running"

        workflow.interrupt_reason = None

        db.commit()

        db.refresh(workflow)

        return workflow