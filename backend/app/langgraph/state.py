from typing import TypedDict
from typing import Optional


class WorkflowState(TypedDict):

    workflow_id: str

    status: str

    current_node: str

    input_data: dict

    execution_plan: Optional[dict]

    execution_result: Optional[dict]

    review_status: Optional[dict]