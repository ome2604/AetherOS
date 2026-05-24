import time

from app.core.celery_app import celery_app
from app.db.session import SessionLocal
from app.services.workflow_service import WorkflowService


@celery_app.task
def execute_workflow(workflow_id: str):

    db = SessionLocal()

    try:
        WorkflowService.update_workflow_status(
            db,
            workflow_id,
            "RUNNING"
        )

        print(f"Starting workflow: {workflow_id}")

        time.sleep(10)

        WorkflowService.update_workflow_status(
            db,
            workflow_id,
            "COMPLETED"
        )

        print(f"Completed workflow: {workflow_id}")

    except Exception:

        WorkflowService.update_workflow_status(
            db,
            workflow_id,
            "FAILED"
        )

    finally:
        db.close()