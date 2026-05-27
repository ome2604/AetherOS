from app.core.redis import RedisManager


class EventBus:

    @staticmethod
    def publish_workflow_event(
        workflow_id: str,
        event_type: str,
        data: dict,
    ):

        RedisManager.publish(
            f"workflow:{workflow_id}",
            {
                "workflow_id": workflow_id,
                "event_type": event_type,
                "data": data,
            },
        )