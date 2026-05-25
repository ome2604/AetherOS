from app.llm.openai_provider import (
    OpenAIProvider,
)


class LLMFactory:

    @staticmethod
    def get_provider(provider: str):

        if provider == "openai":

            return OpenAIProvider()

        raise ValueError(
            f"Unsupported provider: {provider}"
        )