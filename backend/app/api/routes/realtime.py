import asyncio

from fastapi import APIRouter

from fastapi import WebSocket

from fastapi import WebSocketDisconnect

from app.runtime.event_manager import (
    EventManager,
)

router = APIRouter()


@router.websocket(
    "/ws/workflows/{workflow_id}"
)
async def workflow_websocket(

    websocket: WebSocket,

    workflow_id: str,
):

    await EventManager.connect(

        workflow_id,

        websocket,
    )

    try:

        while True:

            # keep connection alive
            await asyncio.sleep(1)

    except WebSocketDisconnect:

        EventManager.disconnect(

            workflow_id,

            websocket,
        )