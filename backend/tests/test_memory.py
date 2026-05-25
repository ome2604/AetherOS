from app.memory.memory_store import (
    MemoryStore,
)

from app.memory.schemas import (
    MemoryRecord,
)

from app.memory.retrieval import (
    MemoryRetriever,
)


def test_memory_storage_and_retrieval():

    store = MemoryStore()

    retriever = MemoryRetriever()

    memory = MemoryRecord(
        workflow_id="test-memory-id",
        task="Revenue calculation",
        execution_plan="Plan",
        execution_result="Result",
        review_result="Success",
    )

    store.store_memory(memory)

    results = retriever.retrieve(
        "Revenue calculation"
    )

    documents = results.get(
        "documents",
        [[]],
    )[0]

    assert len(documents) > 0