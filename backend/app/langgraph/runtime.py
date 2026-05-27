from app.langgraph.nodes import (
    planner_node,
    executor_node,
    reviewer_node,
)


class LangGraphRuntime:

    def __init__(self):

        self.node_map = {

            "planner": planner_node,

            "executor": executor_node,

            "reviewer": reviewer_node,
        }

    def execute_node(
        self,
        node_name: str,
        state: dict,
    ):

        node = self.node_map.get(
            node_name
        )

        if not node:

            raise Exception(
                f"Unknown node: {node_name}"
            )

        return node(state)

    def get_next_node(
        self,
        state: dict,
    ):

        return state.get(
            "current_node",
            "completed",
        )