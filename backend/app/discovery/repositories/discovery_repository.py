from sqlalchemy.orm import Session

from app.models.discovery_session import (
    DiscoverySession,
)

from app.models.discovery_message import (
    DiscoveryMessage,
)

from app.models.project_context import (
    ProjectContext,
)


class DiscoveryRepository:

    # =====================================
    # CREATE SESSION
    # =====================================

    @staticmethod
    def create_session(

        db: Session,

        title: str,
    ):

        session = DiscoverySession(

            title=title
        )

        db.add(session)

        db.commit()

        db.refresh(session)

        return session

    # =====================================
    # GET SESSION
    # =====================================

    @staticmethod
    def get_session(

        db: Session,

        session_id: str,
    ):

        return (

            db.query(
                DiscoverySession
            )

            .filter(
                DiscoverySession.id
                == session_id
            )

            .first()
        )

    # =====================================
    # SAVE MESSAGE
    # =====================================

    @staticmethod
    def save_message(

        db: Session,

        session_id: str,

        role: str,

        content: str,
    ):

        message = DiscoveryMessage(

            session_id=session_id,

            role=role,

            content=content,
        )

        db.add(message)

        db.commit()

        db.refresh(message)

        return message

    # =====================================
    # UPDATE SESSION
    # =====================================

    @staticmethod
    def update_session(

        db: Session,

        session,
    ):

        db.commit()

        db.refresh(session)

        return session

    # =====================================
    # CREATE PROJECT CONTEXT
    # =====================================

    @staticmethod
    def create_project_context(

        db: Session,

        session_id: str,

        project_name: str,

        structured_context: dict,
    ):

        context = ProjectContext(

            discovery_session_id=session_id,

            project_name=project_name,

            structured_context=structured_context,
        )

        db.add(context)

        db.commit()

        db.refresh(context)

        return context