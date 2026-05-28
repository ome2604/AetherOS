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


class ProjectContext(Base):

    __tablename__ = (
        "project_contexts"
    )

    id = Column(

        UUID(as_uuid=True),

        primary_key=True,

        default=uuid.uuid4,
    )

    discovery_session_id = Column(

        UUID(as_uuid=True),

        nullable=False,
    )

    project_name = Column(

        String,

        nullable=False,
    )

    structured_context = Column(

        JSON,

        nullable=False,
    )

    created_at = Column(

        DateTime,

        default=datetime.utcnow,
    )