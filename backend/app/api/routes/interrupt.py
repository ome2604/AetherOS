from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from pydantic import BaseModel

from app.db.session import get_db

from app.services.interrupt_service import (
    InterruptService,
)

router = APIRouter()


class PauseRequest(
    BaseModel
):

    reason: str


@router.post(
    "/workflows/{workflow_id}/pause"
)
def pause_workflow(
    workflow_id: str,
    request: PauseRequest,
    db: Session = Depends(get_db),
):

    workflow = (
        InterruptService
        .pause_workflow(
            db,
            workflow_id,
            request.reason,
        )
    )

    return {

        "workflow_id": workflow.id,

        "status": workflow.status,

        "reason": (
            workflow.interrupt_reason
        ),
    }


@router.post(
    "/workflows/{workflow_id}/resume"
)
def resume_workflow(
    workflow_id: str,
    db: Session = Depends(get_db),
):

    workflow = (
        InterruptService
        .resume_workflow(
            db,
            workflow_id,
        )
    )

    return {

        "workflow_id": workflow.id,

        "status": workflow.status,
    }