from langgraph.graph import (
    StateGraph,
    END,
)

from app.langgraph.state import (
    WorkflowState,
)

from app.langgraph.nodes import (
    planner_node,
    executor_node,
    reviewer_node,
)

from app.langgraph.conditions import (
    should_continue,
)


def build_workflow_graph():

    workflow = StateGraph(
        WorkflowState
    )

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

    workflow.set_entry_point(
        "planner"
    )

    workflow.add_conditional_edges(
        "planner",
        should_continue,
        {
            "executor": "executor",
        },
    )

    workflow.add_conditional_edges(
        "executor",
        should_continue,
        {
            "reviewer": "reviewer",
        },
    )

    workflow.add_edge(
        "reviewer",
        END,
    )

    return workflow.compile()