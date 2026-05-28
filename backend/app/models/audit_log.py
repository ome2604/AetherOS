
import uuid

from sqlalchemy import (

    Column,

    String,

    JSON,

    DateTime,
)

from sqlalchemy.dialects.postgresql import (
    UUID,
)

from sqlalchemy.sql import func

from app.db.base_class import Base


class AuditLog(Base):

    __tablename__ = "audit_logs"

    id = Column(

        UUID(as_uuid=True),

        primary_key=True,

        default=uuid.uuid4,
    )

    entity_type = Column(
        String
    )

    entity_id = Column(
        String
    )

    action = Column(
        String
    )

    actor_id = Column(
        String
    )

    event_metadata = Column(
        JSON
    )

    created_at = Column(

        DateTime(timezone=True),

        server_default=func.now(),
    )
