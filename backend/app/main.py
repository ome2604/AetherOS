from fastapi import FastAPI

from fastapi.middleware.cors import (
    CORSMiddleware,
)

from prometheus_fastapi_instrumentator import (
    Instrumentator,
)

# =========================================
# WORKFLOW ROUTES
# =========================================

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

# =========================================
# DISCOVERY ROUTES
# =========================================

from app.api.routes.discovery import (
    router as discovery_router,
)

from app.api.routes.discovery_ws import (
    router as discovery_ws_router,
)

# =========================================
# FASTAPI APP
# =========================================

app = FastAPI(

    title="AetherOS",

    version="2.4.0",

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

# -----------------------------------------
# WORKFLOW ENGINE
# -----------------------------------------

app.include_router(
    workflow_router
)

# -----------------------------------------
# WEBSOCKET RUNTIME
# -----------------------------------------

app.include_router(
    websocket_router
)

# -----------------------------------------
# REPLAY RUNTIME
# -----------------------------------------

app.include_router(
    replay_router
)

# -----------------------------------------
# INTERRUPT RUNTIME
# -----------------------------------------

app.include_router(
    interrupt_router
)

# -----------------------------------------
# REALTIME RUNTIME
# -----------------------------------------

app.include_router(
    realtime_router
)

# -----------------------------------------
# METRICS RUNTIME
# -----------------------------------------

app.include_router(
    metrics_router
)

# -----------------------------------------
# DISCOVERY ENGINE
# -----------------------------------------

app.include_router(
    discovery_router
)

# -----------------------------------------
# DISCOVERY REALTIME WS
# -----------------------------------------

app.include_router(
    discovery_ws_router
)

# =========================================
# PROMETHEUS METRICS
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

        "version": "2.4.0",

        "phase": (
            "PHASE 2 - "
            "Discovery Intelligence Engine"
        ),
    }

# =========================================
# HEALTH CHECK
# =========================================

@app.get("/health")
def health():

    return {

        "status": "healthy",

        "services": {

            "api":
                "running",

            "workflow_runtime":
                "enabled",

            "interrupt_runtime":
                "enabled",

            "replay_runtime":
                "enabled",

            "realtime_runtime":
                "enabled",

            "metrics_runtime":
                "enabled",

            "discovery_runtime":
                "enabled",

            "discovery_realtime":
                "enabled",

            "websocket_runtime":
                "enabled",

            "checkpoint_runtime":
                "enabled",

            "observability":
                "enabled",
        }
    }

# =========================================
# RUNTIME INFO
# =========================================

@app.get("/runtime")
def runtime_info():

    return {

        "runtime":
            "langgraph",

        "durability":
            "enabled",

        "checkpointing":
            "enabled",

        "replay_runtime":
            "enabled",

        "interrupt_runtime":
            "enabled",

        "realtime_runtime":
            "enabled",

        "metrics_runtime":
            "enabled",

        "event_persistence":
            "enabled",

        "distributed_workers":
            "enabled",

        "discovery_engine":
            "enabled",

        "organizational_memory":
            "enabled",

        "realtime_discovery_workspace":
            "enabled",
    }

# =========================================
# PLATFORM INFO
# =========================================

@app.get("/platform")
def platform_info():

    return {

        "name":
            "AetherOS",

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

            "discovery_engine":
                "AI Discovery Runtime",

            "ai_runtime":
                "OpenAI",
        },

        "capabilities": [

            "Durable Workflows",

            "Replay Runtime",

            "Interrupt Runtime",

            "Realtime Telemetry",

            "Workflow Checkpointing",

            "Distributed Execution",

            "Operational Observability",

            "AI Discovery Sessions",

            "Structured Context Extraction",

            "Discovery State Machine",

            "Realtime AI Streaming",

            "Collaborative Discovery",

            "Live Intelligence Updates",

            "Operational AI Workspace",

            "Organizational Intelligence",
        ],
    }

# =========================================
# DISCOVERY RUNTIME INFO
# =========================================

@app.get("/discovery/runtime")
def discovery_runtime():

    return {

        "status":
            "active",

        "engine":
            "Discovery Intelligence Engine",

        "ai_runtime":
            "OpenAI",

        "realtime_streaming":
            "enabled",

        "state_machine": [

            "collect_goal",

            "collect_users",

            "collect_constraints",

            "collect_scale",

            "collect_integrations",

            "generate_context",
        ],

        "capabilities": [

            "AI Product Discovery",

            "Structured Context Extraction",

            "Business Intelligence Collection",

            "Project Context Generation",

            "Realtime Discovery Streaming",

            "Collaborative AI Discovery",

            "Operational AI Workspace",

            "Organizational Memory",
        ],
    }