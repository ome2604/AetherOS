
from uuid import UUID

from pydantic import BaseModel


# =========================================
# REQUESTS
# =========================================

class CreateWorkspaceRequest(
    BaseModel
):

    name: str

    description: str

    owner_id: str


class AddWorkspaceMemberRequest(
    BaseModel
):

    workspace_id: str

    user_id: str

    role: str


# =========================================
# RESPONSES
# =========================================

class WorkspaceResponse(
    BaseModel
):

    id: UUID

    name: str

    description: str | None = None

    owner_id: str | None = None

    model_config = {
        "from_attributes": True
    }


class WorkspaceMemberResponse(
    BaseModel
):

    id: UUID

    workspace_id: UUID

    user_id: str

    role: str

    model_config = {
        "from_attributes": True
    }
