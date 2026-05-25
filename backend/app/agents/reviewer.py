import asyncio

from app.agents.base import BaseAgent

from app.orchestrator.state import WorkflowState

from app.realtime.websocket_routes import (
    broadcast_event,
)

from app.services.llm_service import (
    LLMService,
)

from app.prompts.reviewer_prompt import (
    REVIEWER_PROMPT,
)

from app.memory.memory_store import (
    MemoryStore,
)

from app.memory.schemas import (
    MemoryRecord,
)


class ReviewerAgent(BaseAgent):

    def __init__(self):

        self.llm_service = LLMService()

        self.memory_store = MemoryStore()

    def run(
        self,
        state: WorkflowState,
    ) -> WorkflowState:

        asyncio.run(
            broadcast_event(
                {
                    "event": "review_started",
                    "workflow_id": str(
                        state["workflow_id"]
                    ),
                }
            )
        )

        task = state["input_data"].get(
            "task",
            "",
        )

        result = state.get(
            "execution_result",
            {},
        )

        prompt = REVIEWER_PROMPT.format(
            task=task,
            result=result,
        )

        response = self.llm_service.generate(
            prompt=prompt
        )

        review_text = response.content.lower()

        state["review_status"] = (
            response.content
        )

        memory = MemoryRecord(
            workflow_id=str(
                state["workflow_id"]
            ),
            task=task,
            execution_plan=str(
                state.get(
                    "execution_plan",
                    ""
                )
            ),
            execution_result=str(
                state.get(
                    "execution_result",
                    ""
                )
            ),
            review_result=response.content,
        )

        self.memory_store.store_memory(
            memory
        )

        if (
            "fail" in review_text
            or "retry" in review_text
            or "incorrect" in review_text
        ):

            state["retry_count"] += 1

            state["status"] = "retrying"

        else:

            state["status"] = "completed"

        state["current_node"] = "completed"

        asyncio.run(
            broadcast_event(
                {
                    "event": "workflow_completed",
                    "workflow_id": str(
                        state["workflow_id"]
                    ),
                    "tokens": response.total_tokens,
                }
            )
        )

        return state