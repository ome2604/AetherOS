from langgraph.graph import (
    StateGraph,
    END,
)

from typing import TypedDict


class DiscoveryState(
    TypedDict
):

    current_step: str

    context: dict

    latest_message: str

    ai_response: str


# =========================================
# NODE
# =========================================

def discovery_node(
    state: DiscoveryState
):

    return {

        "current_step":
            state["current_step"],

        "context":
            state["context"],

        "latest_message":
            state["latest_message"],

        "ai_response":
            "AI discovery processing...",
    }


# =========================================
# GRAPH
# =========================================

workflow = StateGraph(
    DiscoveryState
)

workflow.add_node(
    "discovery",
    discovery_node,
)

workflow.set_entry_point(
    "discovery"
)

workflow.add_edge(
    "discovery",
    END,
)

discovery_graph = (
    workflow.compile()
)