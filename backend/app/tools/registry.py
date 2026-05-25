from app.tools.calculator import (
    CalculatorTool,
)


class ToolRegistry:

    tools = {
        "calculator": CalculatorTool(),
    }

    @classmethod
    def get_tool(cls, tool_name):

        return cls.tools.get(tool_name)