def planner_node(
    state: dict,
):

    task = (
        state["input_data"]
        .get("task")
    )

    state["execution_plan"] = {
        "plan":
            f"Execution plan created for: {task}"
    }

    state["current_node"] = "executor"

    return state


def executor_node(
    state: dict,
):

    plan = (
        state["execution_plan"]
        .get("plan")
    )

    state["execution_result"] = {
        "result":
            f"Executed: {plan}"
    }

    state["current_node"] = "reviewer"

    return state


def reviewer_node(
    state: dict,
):

    result = (
        state["execution_result"]
        .get("result")
    )

    state["review_status"] = {
        "review":
            f"Reviewed result: {result}"
    }

    state["current_node"] = "completed"

    state["status"] = "completed"

    return state