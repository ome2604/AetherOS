from app.repositories.workspace_repository import (
    WorkspaceRepository,
)

from app.services.audit_service import (
    AuditService,
)


class WorkspaceService:

    # =====================================
    # CREATE WORKSPACE
    # =====================================

    @staticmethod
    def create_workspace(

        db,

        request,
    ):

        workspace = (

            WorkspaceRepository
            .create_workspace(

                db=db,

                name=request.name,

                description=(
                    request.description
                ),

                owner_id=(
                    request.owner_id
                ),
            )
        )

        AuditService.log_action(

            db=db,

            entity_type="workspace",

            entity_id=workspace.id,

            action="workspace_created",

            actor_id=request.owner_id,
        )

        return workspace

    # =====================================
    # ADD MEMBER
    # =====================================

    @staticmethod
    def add_member(

        db,

        request,
    ):

        member = (

            WorkspaceRepository
            .add_member(

                db=db,

                workspace_id=(
                    request.workspace_id
                ),

                user_id=request.user_id,

                role=request.role,
            )
        )

        AuditService.log_action(

            db=db,

            entity_type="workspace_member",

            entity_id=member.id,

            action="member_added",

            actor_id=request.user_id,
        )

        return member