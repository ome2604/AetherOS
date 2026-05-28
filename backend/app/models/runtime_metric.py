import uuid

from datetime import datetime

from sqlalchemy import (
    Column,
    String,
    Float,
    DateTime,
)

from sqlalchemy.dialects.postgresql import (
    UUID,
)

from app.db.base_class import Base

class RuntimeMetric(Base):

    __tablename__ = "runtime_metrics"

    id = Column(

        UUID(as_uuid=True),

        primary_key=True,

        default=uuid.uuid4,
    )

    workflow_id = Column(

        UUID(as_uuid=True),

        nullable=False,
    )

    metric_name = Column(

        String,

        nullable=False,
    )

    metric_value = Column(

        Float,

        nullable=False,
    )

    node_name = Column(

        String,

        nullable=True,
    )

    created_at = Column(

        DateTime,

        default=datetime.utcnow,

        nullable=False,
    )