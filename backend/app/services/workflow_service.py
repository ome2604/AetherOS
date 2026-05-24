from sqlalchemy.orm import Session

from app.models.workflow import Workflow


class WorkflowService:

    @staticmethod
    def create_workflow(db: Session, name: str):

        workflow = Workflow(
            name=name,
            status="PENDING"
        )

        db.add(workflow)
        db.commit()
        db.refresh(workflow)

        return workflow

    @staticmethod
    def get_workflow(db: Session, workflow_id):

        return db.query(Workflow).filter(
            Workflow.id == workflow_id
        ).first()

    @staticmethod
    def list_workflows(db: Session):

        return db.query(Workflow).all()

    @staticmethod
    def update_workflow_status(
        db: Session,
        workflow_id,
        status: str
    ):

        workflow = db.query(Workflow).filter(
            Workflow.id == workflow_id
        ).first()

        if workflow:
            workflow.status = status

            db.commit()
            db.refresh(workflow)

        return workflow