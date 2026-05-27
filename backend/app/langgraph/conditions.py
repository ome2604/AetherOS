def should_continue(
    state,
):

    current_node = state.get(
        "current_node"
    )

    if current_node == "executor":

        return "executor"

    if current_node == "reviewer":

        return "reviewer"

    return "end"