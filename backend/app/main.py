import asyncio

import redis.asyncio as redis

from fastapi import FastAPI
from fastapi import WebSocket
from fastapi import WebSocketDisconnect

from prometheus_fastapi_instrumentator import Instrumentator

from app.api.workflows import router
from app.core.config import settings
from app.websockets.manager import manager


app = FastAPI(
    title="AetherOS"
)

Instrumentator().instrument(app).expose(app)

app.include_router(router)


@app.get("/")
async def root():

    return {
        "message": "AetherOS API Running"
    }


@app.websocket("/ws/workflows")
async def websocket_endpoint(
    websocket: WebSocket
):

    await manager.connect(websocket)

    try:

        while True:
            await asyncio.sleep(1)

    except WebSocketDisconnect:

        manager.disconnect(websocket)


async def redis_subscriber():

    redis_client = redis.from_url(
        settings.REDIS_URL
    )

    pubsub = redis_client.pubsub()

    await pubsub.subscribe(
        "workflow-events"
    )

    while True:

        message = await pubsub.get_message(
            ignore_subscribe_messages=True
        )

        if message:

            data = message["data"]

            await manager.broadcast(
                data.decode("utf-8")
            )

        await asyncio.sleep(0.1)


@app.on_event("startup")
async def startup_event():

    asyncio.create_task(
        redis_subscriber()
    )