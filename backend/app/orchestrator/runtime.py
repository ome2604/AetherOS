from langgraph.graph import (
    StateGraph,
)

from app.orchestrator.state import (
    WorkflowState,
)

from app.orchestrator.nodes import (
    planner_node,
    executor_node,
    reviewer_node,
)

from app.orchestrator.router import (
    review_router,
)


class WorkflowRuntime:

    def __init__(self):

        self.graph = (
            self._build_graph()
        )

    def _build_graph(self):

        workflow = StateGraph(
            WorkflowState
        )

        # -----------------------------------
        # NODES
        # -----------------------------------

        workflow.add_node(
            "planner",
            planner_node,
        )

        workflow.add_node(
            "executor",
            executor_node,
        )

        workflow.add_node(
            "reviewer",
            reviewer_node,
        )

        # -----------------------------------
        # ENTRY
        # -----------------------------------

        workflow.set_entry_point(
            "planner"
        )

        # -----------------------------------
        # EDGES
        # -----------------------------------

        workflow.add_edge(
            "planner",
            "executor",
        )

        workflow.add_edge(
            "executor",
            "reviewer",
        )

        # -----------------------------------
        # CONDITIONAL ROUTING
        # -----------------------------------

        workflow.add_conditional_edges(
            "reviewer",
            review_router,
            {
                "retry": "executor",
                "complete": "__end__",
            },
        )

        return workflow.compile()

    def execute(
        self,
        initial_state: WorkflowState,
    ):

        return self.graph.invoke(
            initial_state
        )