import uuid

from datetime import datetime

from sqlalchemy import (
    Column,
    String,
    DateTime,
    JSON,
)

from sqlalchemy.dialects.postgresql import (
    UUID,
)

from app.db.base import Base


class WorkflowEvent(Base):

    __tablename__ = "workflow_events"

    id = Column(

        UUID(as_uuid=True),

        primary_key=True,

        default=uuid.uuid4,
    )

    workflow_id = Column(

        UUID(as_uuid=True),

        nullable=False,
    )

    event_type = Column(

        String,

        nullable=False,
    )

    node_name = Column(

        String,

        nullable=True,
    )

    status = Column(

        String,

        nullable=False,
    )

    payload = Column(

        JSON,

        nullable=True,
    )

    created_at = Column(

        DateTime,

        default=datetime.utcnow,

        nullable=False,
    )