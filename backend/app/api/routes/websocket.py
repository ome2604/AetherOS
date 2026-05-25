from fastapi import (
    APIRouter,
    WebSocket,
    WebSocketDisconnect,
)

from app.realtime.websocket_routes import (
    connect_websocket,
    disconnect_websocket,
)

router = APIRouter()


@router.websocket("/ws/workflows")
async def workflow_websocket(
    websocket: WebSocket,
):

    await connect_websocket(websocket)

    try:

        while True:

            await websocket.receive_text()

    except WebSocketDisconnect:

        disconnect_websocket(websocket)