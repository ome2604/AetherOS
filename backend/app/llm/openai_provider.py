from openai import OpenAI

from app.core.config import settings

from app.llm.base import BaseLLMProvider

from app.llm.schemas import (
    LLMRequest,
    LLMResponse,
)

from app.llm.exceptions import (
    LLMProviderError,
)


class OpenAIProvider(BaseLLMProvider):

    def __init__(self):

        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )

    def generate(
        self,
        request: LLMRequest,
    ) -> LLMResponse:

        try:

            response = self.client.chat.completions.create(
                model=request.model,
                messages=[
                    {
                        "role": "user",
                        "content": request.prompt,
                    }
                ],
                temperature=request.temperature,
            )

            usage = response.usage

            return LLMResponse(
                content=response.choices[0].message.content,
                model=response.model,
                input_tokens=usage.prompt_tokens,
                output_tokens=usage.completion_tokens,
                total_tokens=usage.total_tokens,
            )

        except Exception as e:

            raise LLMProviderError(str(e))