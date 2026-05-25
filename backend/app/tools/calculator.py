from app.tools.base import BaseTool


class CalculatorTool(BaseTool):

    name = "calculator"

    description = "Executes mathematical calculations"

    def execute(self, input_data):

        try:

            result = eval(input_data)

            return str(result)

        except Exception as e:

            return f"Calculation failed: {str(e)}"