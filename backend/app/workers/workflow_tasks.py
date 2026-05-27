from app.workers.celery_app import celery

from app.orchestrator.runtime import (
    WorkflowRuntime,
)

from app.db.session import SessionLocal

from app.models.workflow import Workflow

from app.services.event_bus import (
    EventBus,
)

from app.runtime.recovery_manager import (
    RecoveryManager,
)

from app.runtime.resume_engine import (
    ResumeEngine,
)

from app.runtime.snapshot_manager import (
    SnapshotManager,
)


@celery.task(
    bind=True,

    autoretry_for=(Exception,),

    retry_backoff=True,

    retry_kwargs={"max_retries": 3},
)
def execute_workflow(
    self,
    workflow_id: str,
    task: str,
):

    db = SessionLocal()

    workflow = None

    try:

        workflow = (
            db.query(Workflow)
            .filter(
                Workflow.id == workflow_id
            )
            .first()
        )

        if not workflow:
            return

        workflow.status = "running"

        db.commit()

        EventBus.publish_workflow_event(
            workflow_id,
            "workflow_started",
            {
                "status": "running"
            },
        )

        recovered = (
            RecoveryManager
            .recover_workflow(
                db,
                workflow_id,
            )
        )

        if recovered:

            next_node = (
                ResumeEngine
                .determine_resume_node(
                    recovered
                )
            )

            initial_state = recovered[
                "workflow_state"
            ]

            initial_state[
                "current_node"
            ] = next_node

        else:

            initial_state = {

                "workflow_id": workflow_id,

                "status": "running",

                "current_node": "planner",

                "input_data": {
                    "task": task
                },

                "execution_plan": None,

                "execution_result": None,

                "review_status": None,
            }

        runtime = WorkflowRuntime()

        result = runtime.execute(
            initial_state
        )

        current_node = result.get(
            "current_node",
            "completed",
        )

        SnapshotManager.persist_snapshot(
            db=db,

            workflow_id=workflow_id,

            node_name=current_node,

            state=result,

            status="running",
        )

        if current_node == "planner":

            SnapshotManager.persist_snapshot(
                db=db,

                workflow_id=workflow_id,

                node_name="planner",

                state=result,

                status="running",
            )

        elif current_node == "executor":

            SnapshotManager.persist_snapshot(
                db=db,

                workflow_id=workflow_id,

                node_name="executor",

                state=result,

                status="running",
            )

        elif current_node == "reviewer":

            SnapshotManager.persist_snapshot(
                db=db,

                workflow_id=workflow_id,

                node_name="reviewer",

                state=result,

                status="running",
            )

        workflow.status = "completed"

        db.commit()

        SnapshotManager.persist_snapshot(
            db=db,

            workflow_id=workflow_id,

            node_name="completed",

            state=result,

            status="completed",
        )

        EventBus.publish_workflow_event(
            workflow_id,
            "workflow_completed",
            {
                "status": "completed",

                "result": result,
            },
        )

        return result

    except Exception as e:

        if workflow:

            workflow.status = "failed"

            db.commit()

            SnapshotManager.persist_snapshot(
                db=db,

                workflow_id=workflow_id,

                node_name="failed",

                state={
                    "error": str(e)
                },

                status="failed",
            )

        EventBus.publish_workflow_event(
            workflow_id,
            "workflow_failed",
            {
                "status": "failed",

                "error": str(e),
            },
        )

        raise self.retry(exc=e)

    finally:

        db.close()