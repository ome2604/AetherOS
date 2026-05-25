from app.memory.embeddings import (
    EmbeddingService,
)

from app.memory.chroma_client import (
    ChromaMemoryClient,
)

from app.memory.schemas import (
    MemoryRecord,
)


class MemoryStore:

    def __init__(self):

        self.embedding_service = (
            EmbeddingService()
        )

        self.client = (
            ChromaMemoryClient()
        )

    def store_memory(
        self,
        memory: MemoryRecord,
    ):

        text = f"""
        Task:
        {memory.task}

        Plan:
        {memory.execution_plan}

        Result:
        {memory.execution_result}

        Review:
        {memory.review_result}
        """

        embedding = (
            self.embedding_service.embed(
                text
            )
        )

        self.client.collection.add(
            ids=[memory.workflow_id],
            documents=[text],
            embeddings=[embedding],
            metadatas=[
                {
                    "task": memory.task,
                }
            ],
        )

        return True