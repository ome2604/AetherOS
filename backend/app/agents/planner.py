import asyncio

from app.agents.base import BaseAgent

from app.orchestrator.state import WorkflowState

from app.realtime.websocket_routes import (
    broadcast_event,
)

from app.services.llm_service import (
    LLMService,
)

from app.memory.retrieval import (
    MemoryRetriever,
)

from app.prompts.rag_planner_prompt import (
    RAG_PLANNER_PROMPT,
)


class PlannerAgent(BaseAgent):

    def __init__(self):

        self.llm_service = LLMService()

        self.memory_retriever = (
            MemoryRetriever()
        )

    def format_memories(
        self,
        retrieval_results,
    ):

        try:

            documents = retrieval_results.get(
                "documents",
                [[]],
            )[0]

            if not documents:

                return (
                    "No historical memories found."
                )

            return "\n\n".join(documents)

        except Exception:

            return (
                "No historical memories found."
            )

    def run(
        self,
        state: WorkflowState,
    ) -> WorkflowState:

        asyncio.run(
            broadcast_event(
                {
                    "event": "planner_started",
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

        retrieval_results = (
            self.memory_retriever.retrieve(
                task
            )
        )

        memories = self.format_memories(
            retrieval_results
        )

        print("\n=== RETRIEVED MEMORIES ===")
        print(memories)

        prompt = (
            RAG_PLANNER_PROMPT.format(
                task=task,
                memories=memories,
            )
        )

        response = self.llm_service.generate(
            prompt=prompt
        )

        print("\n=== GENERATED PLAN ===")
        print(response.content)

        state["execution_plan"] = {
            "content": response.content,
            "tokens": response.total_tokens,
            "model": response.model,
            "retrieved_memories": memories,
        }

        state["current_node"] = "executor"

        asyncio.run(
            broadcast_event(
                {
                    "event": "planner_completed",
                    "workflow_id": str(
                        state["workflow_id"]
                    ),
                    "tokens": response.total_tokens,
                }
            )
        )

        return state