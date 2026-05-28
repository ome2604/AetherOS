from app.models.workspace import (
    Workspace,
)

from app.models.workspace_member import (
    WorkspaceMember,
)


class WorkspaceRepository:

    # =====================================
    # CREATE WORKSPACE
    # =====================================

    @staticmethod
    def create_workspace(

        db,

        name,

        description,

        owner_id,
    ):

        workspace = Workspace(

            name=name,

            description=description,

            owner_id=owner_id,
        )

        db.add(workspace)

        db.commit()

        db.refresh(workspace)

        return workspace

    # =====================================
    # ADD MEMBER
    # =====================================

    @staticmethod
    def add_member(

        db,

        workspace_id,

        user_id,

        role,
    ):

        member = WorkspaceMember(

            workspace_id=workspace_id,

            user_id=user_id,

            role=role,
        )

        db.add(member)

        db.commit()

        db.refresh(member)

        return member