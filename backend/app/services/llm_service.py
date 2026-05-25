from app.llm.factory import LLMFactory

from app.llm.schemas import (
    LLMRequest,
)


class LLMService:

    def __init__(self):

        self.provider = (
            LLMFactory.get_provider("openai")
        )

    def generate(
        self,
        prompt: str,
    ):

        request = LLMRequest(
            model="gpt-4o-mini",
            prompt=prompt,
            temperature=0.2,
        )

        return self.provider.generate(request)