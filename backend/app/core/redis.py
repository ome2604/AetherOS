import json
import redis

from app.core.config import settings


redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    decode_responses=True,
)


class RedisManager:

    @staticmethod
    def set_cache(
        key: str,
        value: dict,
        ttl: int = 3600,
    ):

        redis_client.setex(
            key,
            ttl,
            json.dumps(value),
        )

    @staticmethod
    def get_cache(
        key: str,
    ):

        data = redis_client.get(key)

        if not data:
            return None

        return json.loads(data)

    @staticmethod
    def publish(
        channel: str,
        payload: dict,
    ):

        redis_client.publish(
            channel,
            json.dumps(payload),
        )

    @staticmethod
    def subscribe(
        channel: str,
    ):

        pubsub = redis_client.pubsub()

        pubsub.subscribe(channel)

        return pubsub