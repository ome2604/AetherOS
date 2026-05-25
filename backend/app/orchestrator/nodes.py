from app.orchestrator.state import WorkflowState


def start_node(state: WorkflowState):

    print("Starting workflow execution")

    state["status"] = "running"

    return state


def process_node(state: WorkflowState):

    print("Processing workflow")

    user_input = state["input"]

    result = f"AI processed: {user_input}"

    state["output"] = result

    return state


def end_node(state: WorkflowState):

    print("Ending workflow")

    state["status"] = "completed"

    return state