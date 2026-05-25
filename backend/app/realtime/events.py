from app.realtime.connection_manager import manager


async def publish_event(event_type: str, payload: dict):

    message = {
        "event": event_type,
        "payload": payload,
    }

    await manager.broadcast(message)