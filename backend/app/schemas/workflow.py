from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class WorkflowCreate(BaseModel):

    name: str


class WorkflowResponse(BaseModel):

    id: UUID

    name: str

    status: str

    result: str | None = None

    error: str | None = None

    retry_count: str

    max_retries: str

    created_at: datetime

    started_at: datetime | None = None

    completed_at: datetime | None = None

    class Config:
        from_attributes = True