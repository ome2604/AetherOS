import chromadb


class ChromaMemoryClient:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="./memory_db"
        )

        self.collection = (
            self.client.get_or_create_collection(
                name="workflow_memory"
            )
        )