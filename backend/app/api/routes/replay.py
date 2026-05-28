from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.services.replay_service import (
    ReplayService,
)

router = APIRouter()


@router.get(
    "/workflows/{workflow_id}/replay"
)
def replay_workflow(
    workflow_id: str,
    db: Session = Depends(get_db),
):

    replay = (

        ReplayService
        .generate_workflow_replay(
            db,
            workflow_id,
        )
    )

    return replay