import uuid
from datetime import datetime

from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base


class Workflow(Base):
    __tablename__ = "workflows"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    name = Column(String, nullable=False)

    status = Column(
        String,
        default="pending",
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )