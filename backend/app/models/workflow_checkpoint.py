import uuid

from sqlalchemy import (
    Column,
    String,
    JSON,
    DateTime,
    ForeignKey,
)

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.sql import func

from app.db.base_class import Base

class WorkflowCheckpoint(Base):

    __tablename__ = "workflow_checkpoints"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    workflow_id = Column(
        UUID(as_uuid=True),
        ForeignKey("workflows.id"),
        nullable=False,
    )

    node_name = Column(
        String,
        nullable=False,
    )

    workflow_state = Column(
        JSON,
        nullable=False,
    )

    status = Column(
        String,
        nullable=False,
    )

    retry_count = Column(
        String,
        default="0",
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )