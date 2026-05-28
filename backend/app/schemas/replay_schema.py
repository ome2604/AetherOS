from pydantic import BaseModel

from typing import List
from typing import Dict
from typing import Any


class ReplayStep(
    BaseModel
):

    node_name: str

    status: str

    workflow_state: Dict[
        str,
        Any
    ]

    created_at: str


class WorkflowReplay(
    BaseModel
):

    workflow_id: str

    timeline: List[
        ReplayStep
    ]