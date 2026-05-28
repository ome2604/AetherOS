from collections import defaultdict

from fastapi import WebSocket


class EventManager:

    connections = defaultdict(list)

    @classmethod
    async def connect(

        cls,

        workflow_id: str,

        websocket: WebSocket,
    ):

        await websocket.accept()

        cls.connections[
            workflow_id
        ].append(websocket)

        print(
            f"\n[WEBSOCKET CONNECTED]"
            f" workflow={workflow_id}"
        )

    @classmethod
    def disconnect(

        cls,

        workflow_id: str,

        websocket: WebSocket,
    ):

        if websocket in cls.connections[
            workflow_id
        ]:

            cls.connections[
                workflow_id
            ].remove(websocket)

        print(
            f"\n[WEBSOCKET DISCONNECTED]"
            f" workflow={workflow_id}"
        )

    @classmethod
    async def broadcast(

        cls,

        workflow_id: str,

        message: dict,
    ):

        print(
            f"\n[BROADCAST]"
            f" workflow={workflow_id}"
            f" message={message}"
        )

        for websocket in cls.connections[
            workflow_id
        ]:

            await websocket.send_json(
                message
            )