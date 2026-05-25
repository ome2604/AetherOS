from app.orchestrator.state import (
    WorkflowState,
)


def review_router(
    state: WorkflowState,
):

    review = str(
        state.get(
            "review_status",
            ""
        )
    ).lower()

    if (
        "fail" in review
        or "retry" in review
        or "incorrect" in review
    ):

        return "retry"

    return "complete"