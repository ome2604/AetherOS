from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class WorkflowCreate(BaseModel):
    name: str


class WorkflowResponse(BaseModel):
    id: UUID
    name: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True