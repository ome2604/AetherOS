from tests.conftest import client


def test_workflow_execution():

    payload = {
        "task": (
            "Calculate yearly ARR "
            "for 12000 MRR"
        )
    }

    response = client.post(
        "/workflows",
        json=payload,
    )

    assert response.status_code == 200

    data = response.json()

    assert "workflow_id" in data