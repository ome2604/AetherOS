from fastapi import FastAPI

from app.api.workflows import router as workflow_router

app = FastAPI(
    title="AetherOS API",
    version="1.0.0"
)

app.include_router(workflow_router)


@app.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }