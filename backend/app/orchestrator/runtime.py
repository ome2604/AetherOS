from app.orchestrator.nodes import (
    planner_node,
    executor_node,
    reviewer_node,
)


class WorkflowRuntime:

    def __init__(self):

        self.node_map = {

            "planner": planner_node,

            "executor": executor_node,

            "reviewer": reviewer_node,
        }

    def execute(
        self,
        state: dict,
    ):

        current_node = state.get(
            "current_node",
            "planner",
        )

        while current_node != "completed":

            node_executor = self.node_map.get(
                current_node
            )

            if not node_executor:

                raise Exception(
                    f"Unknown node: {current_node}"
                )

            state = node_executor(state)

            current_node = state.get(
                "current_node"
            )

        return state