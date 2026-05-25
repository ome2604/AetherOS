from app.memory.embeddings import (
    EmbeddingService,
)

from app.memory.chroma_client import (
    ChromaMemoryClient,
)


class MemoryRetriever:

    def __init__(self):

        self.embedding_service = (
            EmbeddingService()
        )

        self.client = (
            ChromaMemoryClient()
        )

    def retrieve(
        self,
        query: str,
        limit: int = 3,
    ):

        embedding = (
            self.embedding_service.embed(
                query
            )
        )

        results = (
            self.client.collection.query(
                query_embeddings=[embedding],
                n_results=limit,
            )
        )

        return results