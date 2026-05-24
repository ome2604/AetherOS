from celery import Celery

celery_app = Celery(
    "aetheros",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
    include=["app.tasks.workflow_tasks"]
)

celery_app.conf.update(
    task_track_started=True,
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
    enable_utc=True,
)