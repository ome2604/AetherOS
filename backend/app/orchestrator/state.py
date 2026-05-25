from typing import TypedDict
from uuid import UUID


class WorkflowState(TypedDict):

    workflow_id: UUID

    status: str

    current_node: str

    input_data: dict

    execution_plan: dict

    execution_result: dict

    review_status: str

    retry_count: int