from app.copilots.agents.copilots import (

    product_copilot,

    architecture_copilot,

    planning_copilot,

    risk_copilot,

    execution_copilot,
)


class CopilotOrchestrator:

    # =====================================
    # RUN ALL COPILOTS
    # =====================================

    @staticmethod
    def run(context: str):

        return {

            "product_analysis":

                product_copilot.generate(
                    context
                ),

            "architecture_analysis":

                architecture_copilot.generate(
                    context
                ),

            "planning_analysis":

                planning_copilot.generate(
                    context
                ),

            "risk_analysis":

                risk_copilot.generate(
                    context
                ),

            "execution_analysis":

                execution_copilot.generate(
                    context
                ),
        }