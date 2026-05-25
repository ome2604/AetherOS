from abc import ABC, abstractmethod

from app.llm.schemas import (
    LLMRequest,
    LLMResponse,
)


class BaseLLMProvider(ABC):

    @abstractmethod
    def generate(
        self,
        request: LLMRequest,
    ) -> LLMResponse:

        pass