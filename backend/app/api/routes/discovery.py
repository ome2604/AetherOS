from fastapi import APIRouter

from sqlalchemy.orm import Session

from app.db.session import (
    SessionLocal,
)

from app.discovery.schemas.discovery import (

    StartDiscoveryRequest,

    DiscoveryMessageRequest,
)

from app.discovery.services.discovery_service import (
    DiscoveryService,
)

router = APIRouter(

    prefix="/discovery",

    tags=["Discovery"],
)

# =========================================
# START DISCOVERY
# =========================================

@router.post("/start")
def start_discovery(
    request: StartDiscoveryRequest
):

    db: Session = SessionLocal()

    try:

        result = (

            DiscoveryService
            .start_discovery(

                db=db,

                title=request.title,

                initial_input=(
                    request.initial_input
                ),
            )
        )

        return result

    finally:

        db.close()


# =========================================
# SEND MESSAGE
# =========================================

@router.post("/message")
def send_message(
    request: DiscoveryMessageRequest
):

    db: Session = SessionLocal()

    try:

        result = (

            DiscoveryService
            .process_message(

                db=db,

                session_id=(
                    request.session_id
                ),

                message=request.message,
            )
        )

        return result

    finally:

        db.close()


# =========================================
# GENERATE PROJECT INTELLIGENCE
# =========================================

@router.get(
    "/intelligence/{session_id}"
)
def generate_intelligence(
    session_id: str
):

    db: Session = SessionLocal()

    try:

        result = (

            DiscoveryService
            .generate_project_intelligence(

                db=db,

                session_id=session_id,
            )
        )

        return result

    finally:

        db.close()