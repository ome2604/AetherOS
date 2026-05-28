from collections import defaultdict

from fastapi import WebSocket


class DiscoveryWebSocketManager:

    def __init__(self):

        self.active_connections = (
            defaultdict(list)
        )

    # =====================================
    # CONNECT
    # =====================================

    async def connect(

        self,

        session_id: str,

        websocket: WebSocket,
    ):

        await websocket.accept()

        self.active_connections[
            session_id
        ].append(websocket)

        print(

            f"\n[DISCOVERY WS CONNECTED] "
            f"{session_id}"
        )

    # =====================================
    # DISCONNECT
    # =====================================

    def disconnect(

        self,

        session_id: str,

        websocket: WebSocket,
    ):

        if websocket in (

            self.active_connections[
                session_id
            ]
        ):

            self.active_connections[
                session_id
            ].remove(websocket)

        print(

            f"\n[DISCOVERY WS DISCONNECTED] "
            f"{session_id}"
        )

    # =====================================
    # BROADCAST
    # =====================================

    async def broadcast(

        self,

        session_id: str,

        message: dict,
    ):

        print(

            f"\n[DISCOVERY EVENT] "
            f"{message}"
        )

        dead_connections = []

        for connection in (

            self.active_connections[
                session_id
            ]
        ):

            try:

                await connection.send_json(
                    message
                )

            except Exception:

                dead_connections.append(
                    connection
                )

        for dead in dead_connections:

            self.active_connections[
                session_id
            ].remove(dead)


discovery_ws_manager = (
    DiscoveryWebSocketManager()
)