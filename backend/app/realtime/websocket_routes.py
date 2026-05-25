from fastapi import WebSocket

active_connections = []


async def connect_websocket(
    websocket: WebSocket,
):

    await websocket.accept()

    active_connections.append(websocket)


def disconnect_websocket(
    websocket: WebSocket,
):

    if websocket in active_connections:

        active_connections.remove(websocket)


async def broadcast_event(
    event: dict,
):

    disconnected = []

    for connection in active_connections:

        try:

            await connection.send_json(event)

        except Exception:

            disconnected.append(connection)

    for connection in disconnected:

        if connection in active_connections:

            active_connections.remove(connection)