from fastapi import FastAPI

from fastapi.middleware.cors import (
    CORSMiddleware,
)

from prometheus_fastapi_instrumentator import (
    Instrumentator,
)

from app.api.routes.workflows import (
    router as workflow_router,
)

from app.api.routes.websocket import (
    router as websocket_router,
)

from app.api.routes.replay import (
    router as replay_router,
)

from app.api.routes.interrupt import (
    router as interrupt_router,
)

from app.api.routes.realtime import (
    router as realtime_router,
)

from app.api.routes.metrics import (
    router as metrics_router,
)

app = FastAPI(

    title="AetherOS",

    version="1.0.0",

    description=(
        "Enterprise AI Workflow "
        "Operating System"
    ),
)

# =========================================
# CORS
# =========================================

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

# =========================================
# ROUTES
# =========================================

app.include_router(
    workflow_router
)

app.include_router(
    websocket_router
)

app.include_router(
    replay_router
)

app.include_router(
    interrupt_router
)

app.include_router(
    realtime_router
)

app.include_router(
    metrics_router
)

# =========================================
# METRICS
# =========================================

Instrumentator()\
    .instrument(app)\
    .expose(app)

# =========================================
# ROOT
# =========================================

@app.get("/")
def root():

    return {

        "message": (
            "AetherOS Running"
        ),

        "runtime": "active",

        "platform": (
            "Enterprise AI Workflow "
            "Operating System"
        ),

        "version": "1.0.0",
    }

# =========================================
# HEALTH CHECK
# =========================================

@app.get("/health")
def health():

    return {

        "status": "healthy",

        "services": {

            "api": "running",

            "runtime": "active",

            "observability": "enabled",

            "interrupt_runtime": "enabled",

            "realtime_runtime": "enabled",

            "metrics_runtime": "enabled",

            "workflow_runtime": "enabled",

            "checkpoint_runtime": "enabled",
        }
    }

# =========================================
# RUNTIME INFO
# =========================================

@app.get("/runtime")
def runtime_info():

    return {

        "runtime": "langgraph",

        "durability": "enabled",

        "checkpointing": "enabled",

        "replay_runtime": "enabled",

        "interrupt_runtime": "enabled",

        "realtime_runtime": "enabled",

        "metrics_runtime": "enabled",

        "event_persistence": "enabled",

        "distributed_workers": "enabled",
    }

# =========================================
# PLATFORM INFO
# =========================================

@app.get("/platform")
def platform_info():

    return {

        "name": "AetherOS",

        "type": (
            "Enterprise AI Workflow "
            "Operating System"
        ),

        "architecture": {

            "workflow_engine":
                "LangGraph",

            "task_queue":
                "Celery",

            "database":
                "PostgreSQL",

            "cache":
                "Redis",

            "realtime":
                "WebSockets",

            "observability":
                "Prometheus",
        },

        "capabilities": [

            "Durable Workflows",

            "Replay Runtime",

            "Interrupt Runtime",

            "Realtime Telemetry",

            "Workflow Checkpointing",

            "Distributed Execution",

            "Operational Observability",
        ],
    }