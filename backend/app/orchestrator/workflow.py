from langgraph.graph import StateGraph, END

from app.orchestrator.state import WorkflowState
from app.orchestrator.nodes import (
    start_node,
    process_node,
    end_node,
)


workflow_builder = StateGraph(WorkflowState)

workflow_builder.add_node("start", start_node)
workflow_builder.add_node("process", process_node)
workflow_builder.add_node("end", end_node)

workflow_builder.set_entry_point("start")

workflow_builder.add_edge("start", "process")
workflow_builder.add_edge("process", "end")
workflow_builder.add_edge("end", END)

workflow_graph = workflow_builder.compile()