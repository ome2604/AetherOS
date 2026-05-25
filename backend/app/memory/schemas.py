from pydantic import BaseModel


class MemoryRecord(BaseModel):

    workflow_id: str

    task: str

    execution_plan: str

    execution_result: str

    review_result: str