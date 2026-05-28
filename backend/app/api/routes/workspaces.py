from fastapi import APIRouter

from sqlalchemy.orm import Session

from app.db.session import SessionLocal

from app.schemas.workspace import (
    CreateWorkspaceRequest,
    AddWorkspaceMemberRequest,
    WorkspaceResponse,
    WorkspaceMemberResponse,
)

from app.services.workspace_service import (
    WorkspaceService,
)

router = APIRouter(
    prefix="/workspaces",
    tags=["Collaboration"],
)

# =========================================
# CREATE WORKSPACE
# =========================================

@router.post(
    "/",
    response_model=WorkspaceResponse,
)
def create_workspace(
    request: CreateWorkspaceRequest
):

    db: Session = SessionLocal()

    try:

        workspace = (
            WorkspaceService.create_workspace(
                db=db,
                request=request,
            )
        )

        return WorkspaceResponse(
            id=workspace.id,
            name=workspace.name,
            description=workspace.description,
            owner_id=workspace.owner_id,
        )

    finally:

        db.close()


# =========================================
# ADD MEMBER
# =========================================

@router.post(
    "/members",
    response_model=WorkspaceMemberResponse,
)
def add_member(
    request: AddWorkspaceMemberRequest
):

    db: Session = SessionLocal()

    try:

        member = (
            WorkspaceService.add_member(
                db=db,
                request=request,
            )
        )

        return WorkspaceMemberResponse(
            id=member.id,
            workspace_id=member.workspace_id,
            user_id=member.user_id,
            role=member.role,
        )

    finally:

        db.close()