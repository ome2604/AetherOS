from app.copilots.orchestrator.copilot_orchestrator import (
    CopilotOrchestrator,
)


class CopilotService:

    # =====================================
    # RUN COPILOTS
    # =====================================

    @staticmethod
    def run_copilots(
        context: str
    ):

        return (

            CopilotOrchestrator
            .run(context)
        )