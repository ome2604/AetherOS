import uuid

from app.db.session import (
    SessionLocal,
)

from app.models.workflow import (
    Workflow,
)

from app.langgraph.durable_runtime import (
    DurableLangGraphRuntime,
)

db = SessionLocal()

workflow_id = uuid.uuid4()

workflow = Workflow(

    id=workflow_id,

    name="Durable LangGraph Test",

    status="running",
)

db.add(workflow)

db.commit()

runtime = DurableLangGraphRuntime(
    db
)

initial_state = {

    "workflow_id": str(workflow_id),

    "status": "running",

    "current_node": "planner",

    "input_data": {
        "task":
            "Build enterprise AI payroll system"
    },

    "execution_plan": None,

    "execution_result": None,

    "review_status": None,
}

result = runtime.execute(

    workflow_id=str(workflow_id),

    initial_state=initial_state,
)

print("\nWorkflow completed successfully\n")