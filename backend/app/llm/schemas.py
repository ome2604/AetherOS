from pydantic import BaseModel


class LLMRequest(BaseModel):

    model: str

    prompt: str

    temperature: float = 0.2


class LLMResponse(BaseModel):

    content: str

    model: str

    input_tokens: int

    output_tokens: int

    total_tokens: int