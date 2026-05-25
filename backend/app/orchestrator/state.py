from typing import TypedDict, Optional


class WorkflowState(TypedDict):
    workflow_id: str
    input: str
    output: Optional[str]
    status: str