from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from prometheus_fastapi_instrumentator import Instrumentator

from app.api.routes.workflows import (
    router as workflow_router,
)

from app.api.routes.websocket import (
    router as websocket_router,
)

app = FastAPI(
    title="AetherOS",
)

# =========================
# CORS
# =========================

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

# =========================
# ROUTES
# =========================

app.include_router(workflow_router)

app.include_router(websocket_router)

# =========================
# METRICS
# =========================

Instrumentator().instrument(app).expose(app)

# =========================
# HEALTH
# =========================

@app.get("/")
def root():
    return {
        "message": "AetherOS Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }