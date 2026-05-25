from app.tools.registry import (
    ToolRegistry,
)

from app.tools.schemas import (
    ToolExecutionRequest,
    ToolExecutionResponse,
)


class ToolExecutor:

    @staticmethod
    def execute(
        request: ToolExecutionRequest,
    ) -> ToolExecutionResponse:

        tool = ToolRegistry.get_tool(
            request.tool
        )

        if not tool:

            return ToolExecutionResponse(
                tool=request.tool,
                result="Tool not found",
                success=False,
            )

        result = tool.execute(
            request.input
        )

        return ToolExecutionResponse(
            tool=request.tool,
            result=result,
            success=True,
        )