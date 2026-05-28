from app.copilots.agents.base_copilot import (
    BaseCopilot,
)

from app.copilots.prompts.copilot_prompts import (

    PRODUCT_COPILOT_PROMPT,

    ARCHITECTURE_COPILOT_PROMPT,

    PLANNING_COPILOT_PROMPT,

    RISK_COPILOT_PROMPT,

    EXECUTION_COPILOT_PROMPT,
)


product_copilot = BaseCopilot(
    PRODUCT_COPILOT_PROMPT
)

architecture_copilot = BaseCopilot(
    ARCHITECTURE_COPILOT_PROMPT
)

planning_copilot = BaseCopilot(
    PLANNING_COPILOT_PROMPT
)

risk_copilot = BaseCopilot(
    RISK_COPILOT_PROMPT
)

execution_copilot = BaseCopilot(
    EXECUTION_COPILOT_PROMPT
)