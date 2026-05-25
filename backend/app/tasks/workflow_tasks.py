import time

from app.core.celery_app import celery_app
from app.db.session import SessionLocal
from app.services.workflow_service import WorkflowService
from app.services.event_service import (
    publish_workflow_event
)


@celery_app.task(
    bind=True,
    max_retries=3
)
def execute_workflow(
    self,
    workflow_id: str
):

    db = SessionLocal()

    try:

        WorkflowService.mark_running(
            db,
            workflow_id
        )

        publish_workflow_event(
            workflow_id,
            "RUNNING"
        )

        print(
            f"Starting workflow: {workflow_id}"
        )

        time.sleep(5)

        simulated_failure = False

        if simulated_failure:
            raise Exception(
                "Simulated workflow failure"
            )

        result = "Workflow executed successfully"

        WorkflowService.mark_completed(
            db,
            workflow_id,
            result
        )

        publish_workflow_event(
            workflow_id,
            "COMPLETED"
        )

        print(
            f"Completed workflow: {workflow_id}"
        )

    except Exception as e:

        WorkflowService.increment_retry(
            db,
            workflow_id
        )

        publish_workflow_event(
            workflow_id,
            "RETRYING"
        )

        retry_count = self.request.retries

        print(
            f"Retry attempt: {retry_count}"
        )

        if retry_count < 3:

            raise self.retry(
                exc=e,
                countdown=5
            )

        WorkflowService.mark_failed(
            db,
            workflow_id,
            str(e)
        )

        publish_workflow_event(
            workflow_id,
            "FAILED"
        )

        print(
            f"Workflow permanently failed: {workflow_id}"
        )

    finally:

        db.close()