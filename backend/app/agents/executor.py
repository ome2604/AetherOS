import asyncio
import json
import re

from app.agents.base import BaseAgent

from app.orchestrator.state import WorkflowState

from app.realtime.websocket_routes import (
    broadcast_event,
)

from app.services.llm_service import (
    LLMService,
)

from app.prompts.executor_prompt import (
    EXECUTOR_PROMPT,
)

from app.prompts.tool_prompt import (
    TOOL_SELECTION_PROMPT,
)

from app.tools.executor import (
    ToolExecutor,
)

from app.tools.schemas import (
    ToolExecutionRequest,
)


class ExecutorAgent(BaseAgent):

    def __init__(self):

        self.llm_service = LLMService()

    def extract_json(
        self,
        text: str,
    ):

        try:

            print("\n=== RAW LLM RESPONSE ===")
            print(text)

            match = re.search(
                r"\{[\s\S]*\}",
                text,
            )

            if not match:

                return {
                    "tool": "none",
                    "input": "",
                }

            json_text = match.group(0)

            parsed = json.loads(
                json_text
            )

            print("\n=== PARSED JSON ===")
            print(parsed)

            return parsed

        except Exception as e:

            print(
                f"\nJSON extraction failed: {str(e)}"
            )

            return {
                "tool": "none",
                "input": "",
            }

    def run(
        self,
        state: WorkflowState,
    ) -> WorkflowState:

        asyncio.run(
            broadcast_event(
                {
                    "event": "executor_started",
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

        plan = state.get(
            "execution_plan",
            [],
        )

        tool_prompt = (
            TOOL_SELECTION_PROMPT.format(
                task=task,
                plan=plan,
            )
        )

        tool_response = (
            self.llm_service.generate(
                prompt=tool_prompt
            )
        )

        tool_data = self.extract_json(
            tool_response.content
        )

        if not isinstance(tool_data, dict):

            tool_data = {
                "tool": "none",
                "input": "",
            }

        if "tool" not in tool_data:

            tool_data = {
                "tool": "none",
                "input": "",
            }

        print("\n=== FINAL TOOL DATA ===")
        print(tool_data)

        tool_result = None

        if tool_data["tool"] != "none":

            execution_request = (
                ToolExecutionRequest(
                    tool=tool_data["tool"],
                    input=tool_data["input"],
                )
            )

            tool_execution = (
                ToolExecutor.execute(
                    execution_request
                )
            )

            tool_result = (
                tool_execution.result
            )

            print("\n=== TOOL RESULT ===")
            print(tool_result)

            asyncio.run(
                broadcast_event(
                    {
                        "event": "tool_executed",
                        "workflow_id": str(
                            state["workflow_id"]
                        ),
                        "tool": tool_data["tool"],
                        "result": tool_result,
                    }
                )
            )

        prompt = EXECUTOR_PROMPT.format(
            task=task,
            plan=plan,
        )

        if tool_result:

            prompt += f"""

Tool Result:
{tool_result}
"""

        response = self.llm_service.generate(
            prompt=prompt
        )

        print("\n=== FINAL EXECUTION ===")
        print(response.content)

        state["execution_result"] = {
            "content": response.content,
            "tokens": response.total_tokens,
            "model": response.model,
            "tool_result": tool_result,
        }

        state["current_node"] = "reviewer"

        asyncio.run(
            broadcast_event(
                {
                    "event": "executor_completed",
                    "workflow_id": str(
                        state["workflow_id"]
                    ),
                    "tokens": response.total_tokens,
                }
            )
        )

        return state