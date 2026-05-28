from sqlalchemy.orm import Session

from app.repositories.event_repository import (
    EventRepository,
)


class EventService:

    @staticmethod
    def persist_event(

        db: Session,

        workflow_id: str,

        event_type: str,

        node_name: str,

        status: str,

        payload: dict,
    ):

        return (
            EventRepository.create_event(

                db=db,

                workflow_id=workflow_id,

                event_type=event_type,

                node_name=node_name,

                status=status,

                payload=payload,
            )
        )