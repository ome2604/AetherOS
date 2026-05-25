from pydantic import BaseModel


class ToolExecutionRequest(BaseModel):

    tool: str

    input: str


class ToolExecutionResponse(BaseModel):

    tool: str

    result: str

    success: bool