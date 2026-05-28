from fastapi import APIRouter

from pydantic import BaseModel

from app.copilots.services.copilot_service import (
    CopilotService,
)

router = APIRouter(

    prefix="/copilots",

    tags=["Copilots"],
)


class CopilotRequest(
    BaseModel
):

    context: str


# =========================================
# RUN COPILOTS
# =========================================

@router.post("/run")
def run_copilots(
    request: CopilotRequest
):

    return (

        CopilotService
        .run_copilots(

            context=request.context
        )
    )