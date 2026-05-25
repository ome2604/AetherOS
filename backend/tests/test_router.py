from app.orchestrator.router import (
    review_router,
)


def test_retry_router():

    state = {
        "review_status": (
            "Execution failed. Retry."
        )
    }

    result = review_router(state)

    assert result == "retry"


def test_complete_router():

    state = {
        "review_status": (
            "Execution successful."
        )
    }

    result = review_router(state)

    assert result == "complete"