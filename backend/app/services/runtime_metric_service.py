from sqlalchemy.orm import Session

from app.repositories.runtime_metric_repository import (
    RuntimeMetricRepository,
)


class RuntimeMetricService:

    @staticmethod
    def record_metric(

        db: Session,

        workflow_id: str,

        metric_name: str,

        metric_value: float,

        node_name: str = None,
    ):

        return (

            RuntimeMetricRepository
            .create_metric(

                db=db,

                workflow_id=workflow_id,

                metric_name=metric_name,

                metric_value=metric_value,

                node_name=node_name,
            )
        )

    # =====================================
    # RUNTIME ANALYTICS
    # =====================================

    @staticmethod
    def get_runtime_analytics(
        db: Session
    ):

        avg_duration = (

            RuntimeMetricRepository
            .get_average_workflow_duration(
                db
            )
        )

        failures = (

            RuntimeMetricRepository
            .get_failure_count(
                db
            )
        )

        successes = (

            RuntimeMetricRepository
            .get_success_count(
                db
            )
        )

        return {

            "average_workflow_duration":
                avg_duration,

            "workflow_failures":
                failures,

            "workflow_successes":
                successes,
        }