from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from app.api.routes.workflows import (
    router as workflow_router,
)

from app.api.routes.websocket import (
    router as websocket_router,
)

app = FastAPI(
    title="AetherOS API"
)


@app.get("/")
def root():

    return {
        "message": "AetherOS Runtime Active"
    }


@app.get("/health")
def health_check():

    return {
        "status": "ok"
    }


# ROUTERS
app.include_router(workflow_router)

app.include_router(websocket_router)


# METRICS
Instrumentator().instrument(app).expose(app)