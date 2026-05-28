from sqlalchemy.orm import Session

from app.models.workflow_event import (
    WorkflowEvent,
)


class EventRepository:

    @staticmethod
    def create_event(

        db: Session,

        workflow_id: str,

        event_type: str,

        node_name: str,

        status: str,

        payload: dict,
    ):

        event = WorkflowEvent(

            workflow_id=workflow_id,

            event_type=event_type,

            node_name=node_name,

            status=status,

            payload=payload,
        )

        db.add(event)

        db.commit()

        db.refresh(event)

        return event