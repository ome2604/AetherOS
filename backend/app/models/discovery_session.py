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

from app.db.base_class import Base

class DiscoverySession(Base):

    __tablename__ = (
        "discovery_sessions"
    )

    id = Column(

        UUID(as_uuid=True),

        primary_key=True,

        default=uuid.uuid4,
    )

    title = Column(

        String,

        nullable=False,
    )

    status = Column(

        String,

        default="active",
    )

    current_step = Column(

        String,

        default="collect_goal",
    )

    extracted_context = Column(

        JSON,

        nullable=True,
    )

    created_at = Column(

        DateTime,

        default=datetime.utcnow,
    )