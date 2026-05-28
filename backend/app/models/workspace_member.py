import uuid

from sqlalchemy import (

    Column,

    String,

    DateTime,

    ForeignKey,
)

from sqlalchemy.dialects.postgresql import (
    UUID,
)

from sqlalchemy.sql import func

from app.db.base_class import Base


class WorkspaceMember(Base):

    __tablename__ = (
        "workspace_members"
    )

    id = Column(

        UUID(as_uuid=True),

        primary_key=True,

        default=uuid.uuid4,
    )

    workspace_id = Column(

        UUID(as_uuid=True),

        ForeignKey(
            "workspaces.id"
        ),
    )

    user_id = Column(
        String
    )

    role = Column(
        String
    )

    created_at = Column(

        DateTime(timezone=True),

        server_default=func.now(),
    )