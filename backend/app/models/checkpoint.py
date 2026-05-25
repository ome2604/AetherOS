import uuid
from datetime import datetime

from sqlalchemy import Column, String, DateTime, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base


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

    state = Column(
        JSON,
        nullable=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )