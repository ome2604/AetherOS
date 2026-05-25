from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from app.api.routes.workflows import router as workflow_router


app = FastAPI(title="AetherOS API")


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


app.include_router(workflow_router, prefix="/workflow")


Instrumentator().instrument(app).expose(app)