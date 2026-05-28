from fastapi import (

    APIRouter,

    WebSocket,

    WebSocketDisconnect,
)

from app.discovery.realtime.discovery_ws_manager import (
    discovery_ws_manager,
)

router = APIRouter()

# =========================================
# DISCOVERY WEBSOCKET
# =========================================

@router.websocket(
    "/ws/discovery/{session_id}"
)
async def discovery_websocket(

    websocket: WebSocket,

    session_id: str,
):

    await discovery_ws_manager.connect(

        session_id=session_id,

        websocket=websocket,
    )

    try:

        while True:

            data = await websocket.receive_text()

            await discovery_ws_manager.broadcast(

                session_id=session_id,

                message={

                    "event":
                        "message",

                    "session_id":
                        session_id,

                    "message":
                        data,
                },
            )

    except WebSocketDisconnect:

        discovery_ws_manager.disconnect(

            session_id=session_id,

            websocket=websocket,
        )