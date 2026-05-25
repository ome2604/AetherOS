import uuid

from sqlalchemy import Column, DateTime, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.db.base import Base


class Workflow(Base):

    __tablename__ = "workflows"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    name = Column(
        String,
        nullable=False
    )

    status = Column(
        String,
        nullable=False,
        default="PENDING"
    )

    result = Column(
        Text,
        nullable=True
    )

    error = Column(
        Text,
        nullable=True
    )

    retry_count = Column(
        String,
        nullable=False,
        default="0"
    )

    max_retries = Column(
        String,
        nullable=False,
        default="3"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    started_at = Column(
        DateTime(timezone=True),
        nullable=True
    )

    completed_at = Column(
        DateTime(timezone=True),
        nullable=True
    )