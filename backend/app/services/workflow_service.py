from datetime import datetime

from sqlalchemy.orm import Session

from app.models.workflow import Workflow


class WorkflowService:

    @staticmethod
    def create_workflow(
        db: Session,
        name: str
    ):

        workflow = Workflow(
            name=name,
            status="PENDING",
            retry_count="0",
            max_retries="3"
        )

        db.add(workflow)

        db.commit()

        db.refresh(workflow)

        return workflow

    @staticmethod
    def get_workflow(
        db: Session,
        workflow_id
    ):

        return db.query(Workflow).filter(
            Workflow.id == workflow_id
        ).first()

    @staticmethod
    def list_workflows(db: Session):

        return db.query(Workflow).all()

    @staticmethod
    def mark_running(
        db: Session,
        workflow_id
    ):

        workflow = db.query(Workflow).filter(
            Workflow.id == workflow_id
        ).first()

        if workflow:

            workflow.status = "RUNNING"

            workflow.started_at = datetime.utcnow()

            db.commit()

            db.refresh(workflow)

        return workflow

    @staticmethod
    def mark_completed(
        db: Session,
        workflow_id,
        result: str
    ):

        workflow = db.query(Workflow).filter(
            Workflow.id == workflow_id
        ).first()

        if workflow:

            workflow.status = "COMPLETED"

            workflow.result = result

            workflow.completed_at = datetime.utcnow()

            db.commit()

            db.refresh(workflow)

        return workflow

    @staticmethod
    def mark_failed(
        db: Session,
        workflow_id,
        error: str
    ):

        workflow = db.query(Workflow).filter(
            Workflow.id == workflow_id
        ).first()

        if workflow:

            workflow.status = "FAILED"

            workflow.error = error

            workflow.completed_at = datetime.utcnow()

            db.commit()

            db.refresh(workflow)

        return workflow

    @staticmethod
    def increment_retry(
        db: Session,
        workflow_id
    ):

        workflow = db.query(Workflow).filter(
            Workflow.id == workflow_id
        ).first()

        if workflow:

            workflow.retry_count = str(
                int(workflow.retry_count) + 1
            )

            workflow.status = "RETRYING"

            db.commit()

            db.refresh(workflow)

        return workflow