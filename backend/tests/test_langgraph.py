from app.langgraph.runtime import (
    LangGraphRuntime,
)

runtime = LangGraphRuntime()

initial_state = {

    "workflow_id": "wf-001",

    "status": "running",

    "current_node": "planner",

    "input_data": {
        "task":
            "Build AI fintech payroll platform"
    },

    "execution_plan": None,

    "execution_result": None,

    "review_status": None,
}

result = runtime.execute(
    initial_state
)

print(result)