from pydantic import BaseModel

from typing import Dict
from typing import Any


# =========================================
# START DISCOVERY
# =========================================

class StartDiscoveryRequest(
    BaseModel
):

    title: str

    initial_input: str


# =========================================
# DISCOVERY MESSAGE
# =========================================

class DiscoveryMessageRequest(
    BaseModel
):

    session_id: str

    message: str


# =========================================
# DISCOVERY RESPONSE
# =========================================

class DiscoveryResponse(
    BaseModel
):

    session_id: str

    current_step: str

    ai_response: str

    extracted_context: Dict[
        str,
        Any
    ]


# =========================================
# PROJECT CONTEXT RESPONSE
# =========================================

class ProjectContextResponse(
    BaseModel
):

    session_id: str

    structured_context: Dict[
        str,
        Any
    ]