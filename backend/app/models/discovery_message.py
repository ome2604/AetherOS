import uuid

from datetime import datetime

from sqlalchemy import (
    Column,
    String,
    DateTime,
    Text,
    ForeignKey,
)

from sqlalchemy.dialects.postgresql import (
    UUID,
)

from app.db.base import Base


class DiscoveryMessage(Base):

    __tablename__ = (
        "discovery_messages"
    )

    id = Column(

        UUID(as_uuid=True),

        primary_key=True,

        default=uuid.uuid4,
    )

    session_id = Column(

        UUID(as_uuid=True),

        ForeignKey(
            "discovery_sessions.id"
        ),
    )

    role = Column(

        String,

        nullable=False,
    )

    content = Column(

        Text,

        nullable=False,
    )

    created_at = Column(

        DateTime,

        default=datetime.utcnow,
    )