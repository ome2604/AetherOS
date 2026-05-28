from sqlalchemy import func

from sqlalchemy.orm import Session

from app.models.runtime_metric import (
    RuntimeMetric,
)


class RuntimeMetricRepository:

    @staticmethod
    def create_metric(

        db: Session,

        workflow_id: str,

        metric_name: str,

        metric_value: float,

        node_name: str = None,
    ):

        metric = RuntimeMetric(

            workflow_id=workflow_id,

            metric_name=metric_name,

            metric_value=metric_value,

            node_name=node_name,
        )

        db.add(metric)

        db.commit()

        db.refresh(metric)

        return metric

    # =====================================
    # TOTAL METRICS
    # =====================================

    @staticmethod
    def get_all_metrics(
        db: Session
    ):

        return (
            db.query(
                RuntimeMetric
            )
            .all()
        )

    # =====================================
    # WORKFLOW DURATION
    # =====================================

    @staticmethod
    def get_average_workflow_duration(
        db: Session
    ):

        result = (

            db.query(

                func.avg(
                    RuntimeMetric.metric_value
                )
            )

            .filter(

                RuntimeMetric.metric_name
                == "workflow_duration_seconds"
            )

            .scalar()
        )

        return result or 0

    # =====================================
    # FAILURE COUNT
    # =====================================

    @staticmethod
    def get_failure_count(
        db: Session
    ):

        result = (

            db.query(
                RuntimeMetric
            )

            .filter(

                RuntimeMetric.metric_name
                == "workflow_failure_total"
            )

            .count()
        )

        return result

    # =====================================
    # SUCCESS COUNT
    # =====================================

    @staticmethod
    def get_success_count(
        db: Session
    ):

        result = (

            db.query(
                RuntimeMetric
            )

            .filter(

                RuntimeMetric.metric_name
                == "workflow_success_total"
            )

            .count()
        )

        return result