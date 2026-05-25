import redis
import json

from app.core.config import settings


redis_client = redis.Redis.from_url(
    settings.REDIS_URL
)


def publish_workflow_event(
    workflow_id: str,
    status: str
):

    payload = {
        "workflow_id": workflow_id,
        "status": status
    }

    redis_client.publish(
        "workflow-events",
        json.dumps(payload)
    )