import asyncio
import time

from datetime import datetime

from celery import Celery

from sqlalchemy.orm import Session

from app.db.session import (
    SessionLocal,
)

from app.runtime.event_manager import (
    EventManager,
)

from app.runtime.snapshot_manager import (
    SnapshotManager,
)

from app.runtime.recovery_manager import (
    RecoveryManager,
)

from app.runtime.resume_engine import (
    ResumeEngine,
)

from app.langgraph.durable_runtime import (
    DurableLangGraphRuntime,
)

from app.models.workflow import (
    Workflow,
)

from app.services.event_service import (
    EventService,
)

from app.services.runtime_metric_service import (
    RuntimeMetricService,
)

celery_app = Celery(

    "workflow_tasks",

    broker="redis://localhost:6379/0",

    backend="redis://localhost:6379/0",
)


@celery_app.task
def execute_workflow(

    workflow_id: str,

    task: str,
):

    # =====================================
    # METRICS START TIMER
    # =====================================

    workflow_start_time = time.time()

    db: Session = SessionLocal()

    workflow = None

    try:

        # =====================================
        # LOAD WORKFLOW
        # =====================================

        workflow = (

            db.query(
                Workflow
            )

            .filter(
                Workflow.id == workflow_id
            )

            .first()
        )

        if workflow:

            workflow.status = "running"

            db.commit()

        # =====================================
        # RECOVERY LOGIC
        # =====================================

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

        # =====================================
        # WORKFLOW STARTED EVENT
        # =====================================

        workflow_started_payload = {

            "event": "workflow_started",

            "workflow_id": workflow_id,

            "status": "running",

            "timestamp": (
                datetime.utcnow()
                .isoformat()
            ),
        }

        asyncio.run(

            EventManager.broadcast(

                workflow_id,

                workflow_started_payload,
            )
        )

        EventService.persist_event(

            db=db,

            workflow_id=workflow_id,

            event_type="workflow_started",

            node_name=None,

            status="running",

            payload=workflow_started_payload,
        )

        # =====================================
        # EXECUTE DURABLE RUNTIME
        # =====================================

        runtime = (
            DurableLangGraphRuntime(db)
        )

        result = runtime.execute(

            workflow_id=workflow_id,

            initial_state=initial_state,
        )

        # =====================================
        # FINAL SNAPSHOT
        # =====================================

        SnapshotManager.persist_snapshot(

            db=db,

            workflow_id=workflow_id,

            node_name="completed",

            state=result,

            status="completed",
        )

        # =====================================
        # WORKFLOW COMPLETED EVENT
        # =====================================

        workflow_completed_payload = {

            "event": (
                "workflow_completed"
            ),

            "workflow_id": workflow_id,

            "node": "completed",

            "status": "completed",

            "timestamp": (
                datetime.utcnow()
                .isoformat()
            ),

            "result": result,
        }

        asyncio.run(

            EventManager.broadcast(

                workflow_id,

                workflow_completed_payload,
            )
        )

        EventService.persist_event(

            db=db,

            workflow_id=workflow_id,

            event_type="workflow_completed",

            node_name="completed",

            status="completed",

            payload=workflow_completed_payload,
        )

        # =====================================
        # RECORD METRICS
        # =====================================

        workflow_duration = (
            time.time()
            - workflow_start_time
        )

        RuntimeMetricService.record_metric(

            db=db,

            workflow_id=workflow_id,

            metric_name="workflow_duration_seconds",

            metric_value=workflow_duration,
        )

        RuntimeMetricService.record_metric(

            db=db,

            workflow_id=workflow_id,

            metric_name="workflow_success_total",

            metric_value=1,
        )

        # =====================================
        # UPDATE WORKFLOW STATUS
        # =====================================

        if workflow:

            workflow.status = "completed"

            db.commit()

        return result

    except Exception as e:

        # =====================================
        # FAILED STATUS
        # =====================================

        if workflow:

            workflow.status = "failed"

            db.commit()

        # =====================================
        # FAILURE EVENT
        # =====================================

        workflow_failed_payload = {

            "event": (
                "workflow_failed"
            ),

            "workflow_id": workflow_id,

            "status": "failed",

            "timestamp": (
                datetime.utcnow()
                .isoformat()
            ),

            "error": str(e),
        }

        asyncio.run(

            EventManager.broadcast(

                workflow_id,

                workflow_failed_payload,
            )
        )

        EventService.persist_event(

            db=db,

            workflow_id=workflow_id,

            event_type="workflow_failed",

            node_name=None,

            status="failed",

            payload=workflow_failed_payload,
        )

        # =====================================
        # FAILURE METRICS
        # =====================================

        RuntimeMetricService.record_metric(

            db=db,

            workflow_id=workflow_id,

            metric_name="workflow_failure_total",

            metric_value=1,
        )

        raise e

    finally:

        db.close()