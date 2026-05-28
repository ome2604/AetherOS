from fastapi import APIRouter

from sqlalchemy.orm import Session

from app.db.session import (
    SessionLocal,
)

from app.services.runtime_metric_service import (
    RuntimeMetricService,
)

router = APIRouter(
    prefix="/metrics",
    tags=["Metrics"],
)


# =====================================
# RUNTIME METRICS
# =====================================

@router.get("/runtime")
def runtime_metrics():

    db: Session = SessionLocal()

    try:

        analytics = (

            RuntimeMetricService
            .get_runtime_analytics(
                db
            )
        )

        return {

            "runtime": analytics
        }

    finally:

        db.close()


# =====================================
# WORKFLOW METRICS
# =====================================

@router.get("/workflows")
def workflow_metrics():

    db: Session = SessionLocal()

    try:

        analytics = (

            RuntimeMetricService
            .get_runtime_analytics(
                db
            )
        )

        return {

            "workflow_metrics": {

                "successes":
                    analytics[
                        "workflow_successes"
                    ],

                "failures":
                    analytics[
                        "workflow_failures"
                    ],

                "average_duration":
                    analytics[
                        "average_workflow_duration"
                    ],
            }
        }

    finally:

        db.close()


# =====================================
# FAILURE METRICS
# =====================================

@router.get("/failures")
def failure_metrics():

    db: Session = SessionLocal()

    try:

        analytics = (

            RuntimeMetricService
            .get_runtime_analytics(
                db
            )
        )

        return {

            "failures": {

                "total_failures":
                    analytics[
                        "workflow_failures"
                    ]
            }
        }

    finally:

        db.close()